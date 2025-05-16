FROM python:3.12-slim

RUN pip install --no-cache-dir --upgrade pip flask
WORKDIR /app
COPY ./main.py /app
CMD ["python", "main.py"]
EXPOSE 8000