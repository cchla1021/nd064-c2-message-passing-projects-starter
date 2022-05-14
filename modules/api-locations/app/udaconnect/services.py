import logging
import json
from datetime import datetime, timedelta
from typing import Dict, List
from app import db
from app.udaconnect.models import Location
from app.udaconnect.schemas import LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
from flask import g
from kafka import KafkaConsumer, KafkaProducer, TopicPartition
import sys

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")


class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        location, coord_text = (
            db.session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == location_id)
            .one()
        )

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        return location

    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        kafka_producer = g.kafka_producer
        kafka_producer.send('items', location)
        kafka_consumer = g.kafka_consumer
        tp = TopicPartition('locations',0)
        kafka_consumer.assign([tp])
        lastOffset = kafka_consumer.position(tp)
        kafka_consumer.seek_to_beginning(tp)

        for message in kafka_consumer:
            new_message = message. value
            new_location = Location()
            new location.person_id = new_message['person_id']
            new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
            db.session.add(new_location)
            db.session.commit()
            if message.offset == lastOffset - 1:
               break
        return new_location

    @staticmethod
    def retrieve_all() -> List[Location]:
        return db.session.query(Location).all()
