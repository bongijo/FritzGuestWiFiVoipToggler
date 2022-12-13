FROM python:3.11.1-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY fritz_guest_wifi_voip_toggler.py .

CMD ["python", "/app/fritz_guest_wifi_voip_toggler.py"]
