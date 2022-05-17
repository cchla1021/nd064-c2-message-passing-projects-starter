import time
from concurrent import futures

import grpc
import LocationEvent_pb2
import LocationEvent_pb2_grpc
import logging
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError


class LocationEventServicer(LocationEvent_pb2_grpc.ItemServiceServicer):

        def Create(self, request, context):

            request_value = {
                 "personId": request.personId,
                 "latitude": request.latitude,
                 "longitude": request.longitude,
              }
            print(request_value)
            logging.info('processing entity ', request_value)
            logging.info('Insertion to kafa broker')
            producer = KafkaProducer(bootstrap_servers=['kafka-headless:9092'],api_version=(0, 10, 0),value_serializer=lambda v: json.dumps(v).encode('utf-8'))
            future=producer.send('sample',request_value)
            producer.flush()
            try:
              record_metadata=future.get(timeout=10) 
              print(record_metadata)
            except KafkaError:
              logging.info('Kafka Exception', request_value)
              pass
            return LocationEvent_pb2.LocationEventMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
LocationEvent_pb2_grpc.add_ItemServiceServicer_to_server(LocationEventServicer(), server)
print("gRPC Server listening on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(400)
except KeyboardInterrupt:
    server.stop(0)
