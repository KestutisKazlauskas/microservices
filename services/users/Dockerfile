# Base slim image
FROM python:3.7.4-alpine

# set working directory
WORKDIR /usr/src/app

# Install poetry
RUN pip install "poetry==0.12.17"

# For psycopg2-binary pip library
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Install dependencies
COPY ./poetry.lock  /usr/src/app/poetry.lock
COPY ./pyproject.toml /usr/src/app/pyproject.toml

RUN poetry config settings.virtualenvs.create false && poetry install --no-interaction --no-ansi

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app

# run server for dev only
CMD ["/usr/src/app/entrypoint.sh"]