import pytest
import grpc
import server
import example_pb2
import example_pb2_grpc

@pytest.fixture(scope='module')
def grpc_channel():
    server.serve()
    with grpc.insecure_channel('localhost:50051') as channel:
        yield channel

def test_say_hello(grpc_channel):
    stub = example_pb2_grpc.ExampleServiceStub(grpc_channel)
    request = example_pb2.HelloRequest(name='John')
    response = stub.SayHello(request)
    assert response.message == 'Hello, John!'

if __name__ == '__main__':
    pytest.main(['-sv', __file__])
