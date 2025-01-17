FROM python:3.11-alpine3.20

WORKDIR /app

RUN apk add --no-cache gcc openssh
RUN pip install pipenv --user --no-cache-dir

COPY Pipfile* pyproject.toml /app/
RUN python -m pipenv install \
    && python -m pipenv requirements > requirements.txt \
    && pip install -r requirements.txt --no-cache-dir

COPY . /app
RUN mkdir -p data \
    && mkdir -p media \
    && mkdir -p static
RUN python -m pipenv run migrate \
    && python -m pipenv run collectstatic

EXPOSE 8000

ENTRYPOINT ["python", "-m", "gunicorn"] 
CMD ["config.wsgi", "--bind", "0.0.0.0:8000", "--chdir=/app"]
