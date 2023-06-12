FROM python:3.10.6

RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.psql.txt ./
COPY ./server/requirements.txt ./requirements_server.txt

RUN pip install -r requirements.txt
RUN pip install -r requirements.psql.txt
RUN pip install -r requirements_server.txt

COPY ./ganancias_app ./app
RUN mv ./app/ganancias_pr/local_settings_docker.py ./app/ganancias_pr/local_settings.py

WORKDIR /app

COPY ./server/entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]