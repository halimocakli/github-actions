FROM python:alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN python -v
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

COPY . .

CMD ["python", "/app/main.py"]
