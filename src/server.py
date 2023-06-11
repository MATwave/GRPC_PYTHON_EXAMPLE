import grpc
from concurrent import futures
import example_pb2, example_pb2_grpc

class Greeter(example_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f"Received request: {request.name}")
        response = example_pb2.HelloReply(message=f"Hello, {request.name}!")
        print(f"Sending response: {response.message}")
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server started. Listening on port 50051.")

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)
        print("gRPC server stopped.")

if __name__ == "__main__":
    serve()
