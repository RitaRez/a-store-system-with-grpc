clean:
	rm -r ./bank/*_pb2_grpc.py
	rm -r ./bank/*_pb2.py
	rm -r ./store/*_pb2_grpc.py
	rm -r ./store/*_pb2.py

stubs:
	python3 -m grpc_tools.protoc -I ./bank --python_out=./bank --grpc_python_out=./bank ./bank/bank.proto
#python3 -m grpc_tools.protoc -I ./store --python_out=./store --grpc_python_out=./store ./store/store.proto

run_serv_banco:
	python3 ./bank/bank_server.py $(arg1) $(arg2)

run_cli_banco:
	python3 ./bank/bank_client.py $(arg1) $(arg2)

# run_serv_loja:
#     python3 ./store/store_server.py $(arg1) $(arg2) $(arg3) $(arg4)

# run_cli_loja:
#     python3 ./store/store_client.py $(arg1) $(arg2) $(arg3)