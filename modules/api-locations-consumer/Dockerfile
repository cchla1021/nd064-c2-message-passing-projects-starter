FROM python:3.8

WORKDIR .

COPY . .
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["python", "app/location_event_consumer.py"]
