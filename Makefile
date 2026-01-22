.PHONY: lint docker-test

lint: 
	uv run ruff check . --fix

docker-test:
	docker build -t serverboizbot:tester --target tester . && docker run --rm -it serverboizbot:tester

docker-bot:
	docker build -t serverboizbot:prod --target prod . && docker run --rm --env-file=.env -it serverboizbot:prod 
