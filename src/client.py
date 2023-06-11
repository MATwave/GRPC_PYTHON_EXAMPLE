import grpc
import example_pb2, example_pb2_grpc

def run():
    channel = grpc.insecure_channel("server:50051")
    print("Connecting to gRPC server at server:50051...")

    try:
        grpc.channel_ready_future(channel).result(timeout=10)
        print("Connected to gRPC server successfully.")

        stub = example_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(example_pb2.HelloRequest(name="Alice"))
        print("Response received:", response.message)
    except grpc.FutureTimeoutError as e:
        print("Timeout occurred while connecting to gRPC server.")
    except grpc.RpcError as e:
        print("Error occurred while connecting to gRPC server:", e.details())

if __name__ == "__main__":
    run()
