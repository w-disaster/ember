FROM python:3.11

WORKDIR /usr/app

RUN pip install poetry

COPY . .

RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "-m", "ember.feature_extraction"]