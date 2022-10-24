.PHONY: generate-api-client
openapi.json:
	curl http://localhost:8000/main_server/api/v1/openapi.json > openapi.json

generate: openapi.json
	rm -rf src/resources/npm/api-client
	docker run --rm -v "$(shell pwd):/local" -w /local openapitools/openapi-generator-cli generate \
	    -i openapi.json \
	    -g python \
	    -p packageName=bmlt_client \
	    -p projectName=bmlt-root-server-client \
		--git-repo-id=bmlt-root-server-python-client \
		--git-user-id=bmlt-enabled \
	    -o .

clean:
	rm -f openapi.json
