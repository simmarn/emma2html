# Packages emma2html python application to docker application for easy usage
#FROM python:3-windowsservercore
# using windows nano core image
FROM stefanscherer/python-windows:nano

MAINTAINER Martin Olausson

COPY *.py c:/pyfiles/
COPY html/* c:/pyfiles/html/

WORKDIR c:\\emma2html

ENTRYPOINT ["python", "c:\\pyfiles\\emma2html.py"]
