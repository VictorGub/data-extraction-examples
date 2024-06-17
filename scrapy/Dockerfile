FROM python:3.11 as build

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
gcc

WORKDIR /opt/proj
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
COPY --from=build /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
  libpq5 \
  libxml2 \
  libcurl4 \
  libssl3 \
  libexpat1 \
  libffi-dev \
  zlib1g-dev \
  libxslt1-dev \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/proj
COPY . .
