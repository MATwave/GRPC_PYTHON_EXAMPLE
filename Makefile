up:
	poetry run python -m grpc_tools.protoc -I./proto --python_out=./src --grpc_python_out=./src ./proto/example.proto
	docker compose up -d --build

down:
	rm src/example_pb2.py
	rm src/example_pb2_grpc.py
	docker compose down -v