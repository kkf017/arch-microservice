# BUILDER STAGE
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim AS builder

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app
COPY pyproject.toml poetry.lock ./
COPY microservice ./microservice
RUN touch README.md
RUN poetry install && rm -rf $POETRY_CACHE_DIR

# RUNTIME STAGE
FROM python:${PYTHON_VERSION}-slim-buster AS runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY microservice ./microservice

#CMD python -m service_notifier.main
CMD [ "python",  "-m", "microservice.main" ]
