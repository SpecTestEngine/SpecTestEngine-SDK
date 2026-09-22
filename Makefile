SHELL := /bin/sh

.PHONY: validate generate generate-java generate-typescript generate-python generate-csharp generate-go package package-java package-typescript package-python package-csharp package-go verify clean

validate:
	./scripts/validate.sh

generate:
	./scripts/generate.sh all

generate-java:
	./scripts/generate.sh java

generate-typescript:
	./scripts/generate.sh typescript

generate-python:
	./scripts/generate.sh python

generate-csharp:
	./scripts/generate.sh csharp

generate-go:
	./scripts/generate.sh go

package:
	python3 ./scripts/package-sdk.py --language all

package-java:
	python3 ./scripts/package-sdk.py --language java

package-typescript:
	python3 ./scripts/package-sdk.py --language typescript

package-python:
	python3 ./scripts/package-sdk.py --language python

package-csharp:
	python3 ./scripts/package-sdk.py --language csharp

package-go:
	python3 ./scripts/package-sdk.py --language go

verify:
	./scripts/verify.sh

clean:
	rm -rf clients/java clients/typescript clients/python clients/csharp clients/go artifacts
