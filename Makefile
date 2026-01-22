.PHONY: lint docker-test docker-dev docker-prod

lint: 
	uv run ruff check . --fix

# Run the unit tests in docker exactly like the test pipeline would
docker-test:
	docker build -t serverboizbot:tester --target tester . && docker run --rm -it serverboizbot:tester

# Run the bot in prod mode
docker-prod:
	docker build -t serverboizbot:prod --target prod . && docker run --rm --env-file=.env -it serverboizbot:prod 

# Run the bot with hot reloading
docker-dev:
	docker compose up --watch