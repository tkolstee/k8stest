FROM python:3.12-slim

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY ./main.py /app
CMD ["python", "main.py"]
EXPOSE 8000
