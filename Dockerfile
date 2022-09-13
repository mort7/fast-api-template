# Python 3.9
FROM python:3.9

RUN addgroup --system app && adduser --system --group app

WORKDIR /app/

# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1

# Ensures that python output is sent straight to terminal or container log
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \ 
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* incase it doesn't exist in the repo
COPY pyproject.toml poetry.lock* /app/

ARG INSTALL_DEV=false 

RUN bash -c "if [$INSTALL_DEV] == 'true' ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

# Install Spacy model
RUN poetry run python3 -m spacy download en_core_web_md

COPY ./app /app

ENV PYTHONPATH=/app 

# chown all the files to the app user 
RUN chown -R app:app $HOME

# Change to app user
USER app

# Expose Port 5000
EXPOSE 5000 

# Set working directory
WORKDIR /

# Start gunicorn
CMD ["gunicorn", "--bind=0.0.0.0:5000", "--workers=4", "--worker-class=uvicorn.workers.UvicornWorker", "app.main:app"]