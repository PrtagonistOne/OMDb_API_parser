FROM python:3.9.6-alpine

ENV HOME=/src/omdb_root
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR $HOME

RUN mkdir -p $HOME/omdb
RUN mkdir -p $HOME/scripts

COPY requirements.txt .
COPY omdb $HOME/omdb
COPY scripts $HOME/scripts


RUN apk update \
        && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


RUN chmod +x $HOME/scripts/*

COPY ./scripts/start.sh $HOME/scripts/entrypoint.sh
RUN sed -i 's/\r$//g' $HOME/scripts/entrypoint.sh
RUN chmod +x $HOME/scripts/entrypoint.sh


ENTRYPOINT ["/src/omdb_root/scripts/entrypoint.sh"]