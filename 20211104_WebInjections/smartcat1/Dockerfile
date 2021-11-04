FROM python:2

RUN adduser --home /chall --no-create-home --disabled-password --gecos '' chall

RUN apt update && \
apt-get install -y uwsgi && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

USER chall

WORKDIR /chall
