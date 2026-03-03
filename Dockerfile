# docker build -t lindra/gira .
# docker run lindra/gira

FROM debian:bullseye-slim

ENV LC_ALL=C
ENV container=docker
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y --no-install-recommends python3 && \
    apt clean

RUN apt install -y make wget unzip && apt clean

RUN mkdir /api /hsl
RUN wget https://partner.gira.com/data3/Gira_HomeServer_SDK_Doku.zip -O /t.zip && \
    unzip /t.zip -d /api && \
    rm /t.zip

# basedir is /hsl, projects should be mounted to /hsl/projects
RUN mv '/api/Gira HomeServer SDK Doku/HSL/HSL3 SDK 3.0/generator/generator3.cpython-39.pyc' /hsl/generator.pyc
RUN chmod a+x /hsl/generator.pyc
