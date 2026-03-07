# docker build -t lindra/gira .
# docker run lindra/gira

FROM debian:bullseye-slim

ENV LC_ALL=C
ENV container=docker
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y --no-install-recommends python2 && \
    apt clean

RUN apt install -y make wget unzip && apt clean

RUN mkdir /api
RUN wget https://www.hs-help.net/hshelp/gira/other_documentation/Schnittstelleninformationen.zip -O /t.zip && \
    unzip /t.zip -d /api && \
    rm /t.zip

# basedir is /hsl, projects should be mounted to /hsl/projects
RUN mv '/api/HSL/HSL2 SDK 2.0.7/framework' /hsl
RUN chmod a+x /hsl/generator.pyc
