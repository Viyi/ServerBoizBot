# Install uv
FROM python:3.11-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable

# Copy the project into the intermediate image
COPY . /app

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable


FROM builder AS tester

CMD ["/app/.venv/bin/pytest", "tests"]

FROM python:3.11-slim AS prod
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY ./src /app/src 

CMD ["/app/.venv/bin/serverboizbot"]