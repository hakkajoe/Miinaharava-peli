FROM python:3.9

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

COPY . .

RUN poetry run invoke build

CMD ["poetry", "run", "invoke", "start"]
