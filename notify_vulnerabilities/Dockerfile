FROM python:3.9-slim

WORKDIR /app

COPY notify_vulnerabilities.py /app/notify_vulnerabilities.py
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "notify_vulnerabilities.py"]
