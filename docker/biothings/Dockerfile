# syntax=docker/dockerfile:1.2

ARG PYTHON_VERSION=3.6
FROM library/python:${PYTHON_VERSION}

# cache pip
RUN --mount=type=cache,target=/root/.cache

RUN pip install biothings[hub,web_extra] && pip uninstall -y biothings

RUN pip install "bitarray==0.8.1" "generateDS>=2.29.24" "PyVCF>=0.6.7" "pysam>=0.8.1"

ENV SRC_URI=mongodb://mongodb:27017
ENV SRC_DB=biothings_src
ENV TARGET_URI=mongodb://mongodb:27017
ENV TARGET_DB=biothings_target
ENV HUB_URI=mongodb://mongodb:27017
ENV HUB_DB=biothings_hub

WORKDIR /biothings

ADD ./docker/biothings/configs/* .
ADD . .


CMD [ "sleep", "infinity" ]
