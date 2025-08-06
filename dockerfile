FROM python:3.13.5-slim-bullseye

# Install Poetry
RUN pip install --no-cache-dir poetry

# Create a virtual environment
RUN python -m venv /opt/venv

ENV PATH=/opt/venv/bin:$PATH

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code
WORKDIR /code

COPY pyproject.toml poetry.lock* /code/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY ./src /code

COPY boot/docker-run.sh /opt/run.sh
RUN chmod +x /opt/run.sh

RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["/opt/run.sh"]