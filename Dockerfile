FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY /api /code/api

EXPOSE 11111

CMD ["python", "-u", "api/src/main/server.py"]