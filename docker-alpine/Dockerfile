# Packages emma2html python application to docker application for easy usage
FROM python:3-alpine

MAINTAINER Martin Olausson

COPY *.py /pyfiles/
COPY html/* /pyfiles/html/

WORKDIR /usr/emma2html

ENTRYPOINT ["python", "/pyfiles/emma2html.py"]
