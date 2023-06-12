FROM python:3.10.12-alpine3.18

RUN pip install --upgrade pip

COPY ./requirements.txt .
COPY ./server/requirements.txt ./requirements_server.txt
RUN pip install -r requirements.txt
RUN pip install -r requirements_server.txt

COPY . /app

WORKDIR /app

COPY ./server/entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]