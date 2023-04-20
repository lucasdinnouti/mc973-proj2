FROM python:3.7.12-alpine

WORKDIR /app

COPY ./main.py /app/main.py
COPY ./modules /app/modules

CMD [ "python3", "main.py"]