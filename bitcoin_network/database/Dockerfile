FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip
RUN pip install pipenv

ENV PROJECT_DIR /usr/src/uporabniki_api

WORKDIR ${PROJECT_DIR}

RUN mkdir uploads

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y libffi-dev libfuzzy-dev libfuzzy2 && rm -rf /var/lib/apt/lists/*

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 5000

CMD ["pipenv", "run", "python", "wsgi.py"]
