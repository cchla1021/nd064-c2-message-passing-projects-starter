import grpc
import LocationEvent_pb2
import LocationEvent_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:30003")
stub = LocationEvent_pb2_grpc.ItemServiceStub(channel)

# Update this with desired payload
location = LocationEvent_pb2.LocationEventMessage(
    personId=1222,
    latitude=100,
    longitude=200
   
)


response = stub.Create(location)
