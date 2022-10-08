FROM alpine:latest

RUN apk add python3
RUN apk add py3-pip

COPY . .

RUN pip3 --no-cache-dir install -r requirements.txt