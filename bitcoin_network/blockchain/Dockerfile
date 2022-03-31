FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip
RUN pip install pipenv

ENV PROJECT_DIR /usr/src/uporabniki_api

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 5001

CMD ["pipenv", "run", "python", "wsgi.py"]
