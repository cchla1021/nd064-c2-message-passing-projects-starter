import grpc
import person_pb2
import person_pb2_grpc



print("Retrieving persons data...")

channel = grpc.insecure_channel("localhost:5005")
stub = person_pb2_grpc.PersonServiceStub(channel)

response = stub.Get(person_pb2.Empty())
print(response)
