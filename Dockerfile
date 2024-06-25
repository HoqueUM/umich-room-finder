FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirments.txt

RUN pip install --no-cache-dir -r /app/requirments.txt

COPY ./container /app/container

EXPOSE 69

CMD ["uvicorn", "container.server:app", "--host", "0.0.0.0", "--port", "69"]
