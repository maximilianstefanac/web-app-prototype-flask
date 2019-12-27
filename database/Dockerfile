FROM postgres

RUN apt-get update
RUN apt-get -y -q install postgis

ENV POSTGRES_USER geoapp
ENV POSTGRES_PASSWORD Welcome1!
ENV POSTGRES_DB geoapp

COPY init.sql /docker-entrypoint-initdb.d/