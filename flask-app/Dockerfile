FROM python:3.12-slim

WORKDIR /app
COPY ./main.py ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
EXPOSE 8000