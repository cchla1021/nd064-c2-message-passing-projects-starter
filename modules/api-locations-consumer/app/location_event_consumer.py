import json
import os
from kafka import KafkaConsumer
from sqlalchemy import create_engine

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]
KAFKA_URL = os.environ["KAFKA_URL"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=[KAFKA_URL],group_id=None,auto_offset_reset='earliest')


def write_in_db(location):
    

    engine = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
    conn = engine.connect()

    person_id = int(location["personId"])
    latitude, longitude = int(location["latitude"]), int(location["longitude"])

    insert = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))" \
        .format(person_id, latitude, longitude)

    conn.execute(insert)


for location in consumer:
    message = location.value.decode('utf-8')
    location_message = json.loads(message)
    write_in_db(location_message)
  
