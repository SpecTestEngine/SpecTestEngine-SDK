using SpecTestEngine.Sdk.Workflows;

var attempts = 0;
var value = await WorkflowSupport.PollAsync(
    _ => Task.FromResult(++attempts),
    candidate => candidate == 3,
    new PollOptions(
        TimeSpan.FromMilliseconds(1),
        TimeSpan.FromMilliseconds(1),
        TimeSpan.FromSeconds(1),
        1));
if (value != 3)
{
    throw new InvalidOperationException("Polling did not return the terminal value.");
}

var parser = new SseParser();
parser.Accept("event: progress");
parser.Accept("data: first");
parser.Accept("data: second");
var sseEvent = parser.Accept(string.Empty);
if (sseEvent is null || sseEvent.Data != "first\nsecond")
{
    throw new InvalidOperationException("SSE multiline data was not preserved.");
}

Console.WriteLine("C# workflow helper tests passed.");
