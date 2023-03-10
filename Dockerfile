FROM python:3.12.0-alpine3.14


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Setup working directory
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y default-libmysqlclient-dev gcc && rm -rf /var/lib/apt/lists/*

COPY . /app/

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]

