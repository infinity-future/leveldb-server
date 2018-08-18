FROM ubuntu:18.04

MAINTAINER infinityfuture@foxmail.com

RUN apt-get update
RUN apt-get install -y build-essential git python3-pip
RUN git clone https://github.com/infinityfuture/leveldb-server /leveldbs
RUN pip3 install plyvel

WORKDIR /leveldbs


