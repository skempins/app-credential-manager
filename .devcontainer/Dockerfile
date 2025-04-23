FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

COPY /app/requirements.txt /tmp
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

WORKDIR /app
COPY app/* .

EXPOSE 5000

ENTRYPOINT [ "python3", "/app/app.py" ]