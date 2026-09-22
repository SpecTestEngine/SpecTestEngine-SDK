using System.Runtime.CompilerServices;
using System.Text;

namespace SpecTestEngine.Sdk.Workflows;

public sealed record PollOptions(
    TimeSpan Interval,
    TimeSpan MaximumInterval,
    TimeSpan Timeout,
    double Backoff = 1.5)
{
    public static PollOptions Default { get; } = new(
        TimeSpan.FromMilliseconds(500),
        TimeSpan.FromSeconds(5),
        TimeSpan.FromMinutes(2));

    public void Validate()
    {
        if (Interval <= TimeSpan.Zero || MaximumInterval < Interval || Timeout <= TimeSpan.Zero || Backoff < 1)
        {
            throw new ArgumentOutOfRangeException(nameof(PollOptions), "Polling intervals, timeout, and backoff must be valid.");
        }
    }
}

public sealed class WorkflowTimeoutException : TimeoutException
{
    public WorkflowTimeoutException()
        : base("Workflow did not reach a terminal state before the timeout.")
    {
    }
}

public static class WorkflowSupport
{
    public static async Task<T> PollAsync<T>(
        Func<CancellationToken, Task<T>> fetchValue,
        Func<T, bool> isTerminal,
        PollOptions? options = null,
        Action<T>? onUpdate = null,
        CancellationToken cancellationToken = default)
    {
        ArgumentNullException.ThrowIfNull(fetchValue);
        ArgumentNullException.ThrowIfNull(isTerminal);
        options ??= PollOptions.Default;
        options.Validate();
        var deadline = DateTimeOffset.UtcNow + options.Timeout;
        var delay = options.Interval;

        while (true)
        {
            cancellationToken.ThrowIfCancellationRequested();
            var value = await fetchValue(cancellationToken).ConfigureAwait(false);
            onUpdate?.Invoke(value);
            if (isTerminal(value))
            {
                return value;
            }
            if (DateTimeOffset.UtcNow >= deadline)
            {
                throw new WorkflowTimeoutException();
            }
            await Task.Delay(delay, cancellationToken).ConfigureAwait(false);
            delay = TimeSpan.FromMilliseconds(Math.Min(
                options.MaximumInterval.TotalMilliseconds,
                Math.Max(delay.TotalMilliseconds, delay.TotalMilliseconds * options.Backoff)));
        }
    }

    public static async Task<long> CopyAsync(
        Stream source,
        Stream target,
        long maximumBytes,
        IProgress<long>? progress = null,
        CancellationToken cancellationToken = default)
    {
        ArgumentNullException.ThrowIfNull(source);
        ArgumentNullException.ThrowIfNull(target);
        if (maximumBytes <= 0)
        {
            throw new ArgumentOutOfRangeException(nameof(maximumBytes));
        }
        var buffer = new byte[64 * 1024];
        long total = 0;
        int read;
        while ((read = await source.ReadAsync(buffer, cancellationToken).ConfigureAwait(false)) > 0)
        {
            total += read;
            if (total > maximumBytes)
            {
                throw new IOException("Stream exceeded the configured byte limit.");
            }
            await target.WriteAsync(buffer.AsMemory(0, read), cancellationToken).ConfigureAwait(false);
            progress?.Report(total);
        }
        return total;
    }

    public static async IAsyncEnumerable<SseEvent> ReadSseAsync(
        Stream source,
        [EnumeratorCancellation] CancellationToken cancellationToken = default)
    {
        ArgumentNullException.ThrowIfNull(source);
        using var reader = new StreamReader(
            source,
            Encoding.UTF8,
            detectEncodingFromByteOrderMarks: true,
            bufferSize: 1024,
            leaveOpen: true);
        var parser = new SseParser();
        while (await reader.ReadLineAsync(cancellationToken).ConfigureAwait(false) is { } line)
        {
            if (parser.Accept(line) is { } value)
            {
                yield return value;
            }
        }
        if (parser.Finish() is { } finalValue)
        {
            yield return finalValue;
        }
    }
}

public sealed record SseEvent(string Event, string Data, string? Id = null, long? RetryMilliseconds = null);

public sealed class SseParser
{
    private readonly List<string> data = [];
    private string? eventName;
    private string? id;
    private long? retryMilliseconds;

    public SseEvent? Accept(string line)
    {
        ArgumentNullException.ThrowIfNull(line);
        if (line.Length == 0)
        {
            return Dispatch();
        }
        if (line.StartsWith(':'))
        {
            return null;
        }
        var separator = line.IndexOf(':');
        var field = separator < 0 ? line : line[..separator];
        var value = separator < 0 ? string.Empty : line[(separator + 1)..];
        if (value.StartsWith(' '))
        {
            value = value[1..];
        }
        switch (field)
        {
            case "event": eventName = value; break;
            case "data": data.Add(value); break;
            case "id": id = value; break;
            case "retry" when long.TryParse(value, out var retry) && retry >= 0: retryMilliseconds = retry; break;
        }
        return null;
    }

    public SseEvent? Finish() => Dispatch();

    private SseEvent? Dispatch()
    {
        if (data.Count == 0 && eventName is null && id is null && retryMilliseconds is null)
        {
            return null;
        }
        var result = new SseEvent(eventName ?? "message", string.Join('\n', data), id, retryMilliseconds);
        data.Clear();
        eventName = null;
        retryMilliseconds = null;
        return result;
    }
}
