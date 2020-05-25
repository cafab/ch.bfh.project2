# pull official base image
FROM python:3.8.1-slim-buster

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements.txt
COPY ./requirements.txt .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . /app

# set work directory
WORKDIR /app

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "app.py"]

