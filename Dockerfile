FROM alpine:3.10

MAINTAINER Muhammed Iqbal <iquzart@hotmail.com>

RUN apk add --no-cache python3 py3-pip
#RUN pip3 install < requirements.txt

ENV AWS_ACCESS_KEY_ID "*null*"
ENV AWS_SECRET_ACCESS_KEY "*null*"
ENV AWS_DEFAULT_REGION "*null*"
ENV ARCHIVE_SOURCE "*null*"

COPY . /src/
WORKDIR /src

RUN pip3 install -r requirements.txt

RUN mkdir /tmp/test; echo "this is my test file" > /tmp/test/backup.txt

CMD ["python3","archive.py"]
