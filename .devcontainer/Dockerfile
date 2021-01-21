FROM ubuntu:focal

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y --no-install-recommends install python3 python3-pip

COPY requirements.txt /tmp/pip-reqs/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-reqs/requirements.txt
