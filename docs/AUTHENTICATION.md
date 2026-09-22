# Authentication

Every SpecTestEngine API request made through an SDK requires a short-lived OAuth 2.0 bearer
access token. Generating a client, reading the OpenAPI contract, and browsing the public
documentation do not require a token.

## Choose an access model

| Integration | Use | Recommended flow |
|---|---|---|
| Web, desktop, or mobile application acting for a signed-in user | The user reviews and authorizes access to their SpecTestEngine workspace | Authorization Code with PKCE |
| CI pipeline, scheduled job, backend service, or command-line automation | The integration acts as itself without an interactive user | Client Credentials |

Do not reuse browser session cookies or personal credentials in an SDK integration.

## Obtain integration credentials

Ask a SpecTestEngine company administrator to register the integration. SpecTestEngine Support
can assist an administrator with preview integration registration.

The Integration Builder shows only capabilities available to the company's current subscription.
An administrator selects the required capabilities and approves the resulting scopes. The chosen
integration type determines the OAuth flow and credential form; the subscription determines which
product capabilities can be granted.

The resulting integration details contain only the values needed by the selected flow:

- an issuer URL and client id;
- registered redirect URIs for an interactive application; or
- a one-time client secret for an unattended integration;
- the API audience and scopes approved for the integration.

An access token never expands the subscription. Every request is checked against both the token's
approved permissions and the capabilities currently available to the company. If a capability is
not included in the subscription, requesting or retaining a similarly named scope does not enable
it. After a subscription or integration grant changes, review the integration in the builder and
obtain a new token before using newly available capabilities.

Store a client secret in a deployment secret store. It must not be committed to source control,
included in an SDK archive, embedded in a browser application, or written to logs.

## Discover OAuth endpoints

OAuth endpoints are published through the issuer discovery document:

```text
https://auth.ste.software/.well-known/openid-configuration
```

Use the `authorization_endpoint` and `token_endpoint` returned by discovery instead of hardcoding
provider-specific paths.

## Interactive applications

Use Authorization Code with PKCE when an application acts for a user:

1. Generate a fresh `state`, PKCE `code_verifier`, and `code_challenge` for the sign-in attempt.
2. Open the discovered authorization endpoint with the issued client id, registered redirect URI,
   approved scopes, API audience, and `code_challenge`.
3. Verify `state` on the callback.
4. Exchange the authorization code and `code_verifier` at the discovered token endpoint.
5. Keep access tokens in memory where practical and use the OAuth library's supported refresh
   mechanism when a refresh token was issued.

Use a maintained OAuth/OIDC library for the target platform. Do not implement PKCE, callback
validation, or token parsing manually.

## Unattended integrations

Use Client Credentials for CI and server-to-server automation. Read all values from a secret
store or protected environment variables:

```bash
export STE_BASE_URL="https://app.ste.software"
export STE_TOKEN_URL="<token_endpoint from discovery>"
export STE_CLIENT_ID="<issued client id>"
export STE_CLIENT_SECRET="<one-time issued secret>"
export STE_SCOPE="<approved scopes>"
export STE_AUDIENCE="<approved API audience>"

curl --fail-with-body \
  --user "${STE_CLIENT_ID}:${STE_CLIENT_SECRET}" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "grant_type=client_credentials" \
  --data-urlencode "scope=${STE_SCOPE}" \
  --data-urlencode "audience=${STE_AUDIENCE}" \
  "${STE_TOKEN_URL}"
```

The response contains `access_token`, `token_type`, and its validity period. Cache the token only
until shortly before it expires; do not request a new token for every API call.

## Call the API

Pass only the access token to the generated SDK:

```http
Authorization: Bearer <access-token>
```

The token carries the approved company/project context and scopes. Public API requests must not
add internal owner or actor identifiers. Successful authorization requires all of the following:

1. a valid token for the SpecTestEngine API;
2. the scope required by the operation;
3. the corresponding capability in the company's current subscription.

## Handle expiration and access errors

- `401 Unauthorized`: the token is missing, expired, malformed, issued by the wrong authority, or
  intended for another API. Refresh or reacquire it once, then retry only an idempotent operation.
- `403 Forbidden`: authentication succeeded, but the integration lacks a required permission or
  access to the selected workspace, or the capability is unavailable in the current subscription.
  Do not repeatedly retry; ask an administrator to review the integration grant and subscription.
- `429 Too Many Requests`: respect `Retry-After` and apply bounded backoff.

Rotate a leaked or exposed client secret immediately. Disabling the integration prevents new
authorized work; already issued access tokens naturally stop being accepted according to their
short lifetime and the platform's enforcement policy.

## Production checklist

- Request only the scopes required by the integration.
- Use HTTPS for every production redirect and API call.
- Validate callback `state` and use PKCE for every interactive authorization.
- Keep machine credentials in a secret manager and tokens out of logs and telemetry.
- Use an access-token callback in long-running SDK clients so tokens can be refreshed safely.
- Keep separate credentials for development, staging, and production.
- Rotate credentials when ownership changes or exposure is suspected.
