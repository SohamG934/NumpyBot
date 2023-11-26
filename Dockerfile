FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --default-timeout=100 future

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]