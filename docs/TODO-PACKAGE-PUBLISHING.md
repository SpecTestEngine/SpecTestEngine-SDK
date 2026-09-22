# Package registry publication TODO

Registry publication is intentionally deferred during the SDK package preview. The public source
repository, canonical contract, five generated clients, workflow helpers, and deterministic ZIP
archives can be used without a package registry.

Before public release:

- publish Java artifacts to Maven Central with signing, sources, Javadoc, and provenance;
- publish `@spectestengine/sdk` and the workflow helper to npm with trusted publishing;
- publish Python distributions to PyPI with attestations;
- publish signed C# packages to NuGet;
- tag the Go module at `github.com/SpecTestEngine/SpecTestEngine-SDK/clients/go`;
- attach all deterministic SDK ZIP files and SHA-256 sidecars to the matching GitHub release;
- run installation smoke tests from each candidate registry, not from the workspace;
- publish an SBOM and the exact OpenAPI contract beside every release.

Do not add credentials to generator configs or repository secrets until package names, signing
identities, and the ownership recovery process are finalized.
