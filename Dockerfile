FROM ubuntu:20.04

LABEL maintainer="Trent Nielsen <notgettingmypersonalemail@no.com>"


ENV PYTHON_MODULES \
  docker-py

ENV DEPENDENCIES \
  python3.7 \
  python3-pip

ENV FLASK_APP=memegenerator.py
ENV FLASK_DEBUG=0

# Do PKG stuff
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends $DEPENDENCIES

# Install and upgrade Python PIP, then install some more modules.
RUN pip3 install --upgrade pip
RUN pip3 install setuptools
RUN pip3 install $PYTHON_MODULES
# Copy the requirements file into the container so it knows what PIP packages need to be installed
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./ ./app
WORKDIR ./app
