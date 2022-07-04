import threading, re, grpc, sys

from secrets import token_bytes
from concurrent import futures

sys.path.append('./bank')
from bank_pb2_grpc import *
from bank_pb2 import *
from store_pb2_grpc import *
from store_pb2 import *

class StoreServer (StoreServicer):

    def __init__(self, stop_event, product_value, wallet_key, bank_server_endpoint):
        
        
        self._product_value = int(product_value)
        self._wallet_key = wallet_key
        
        self._stop_event = stop_event
        self._bank_channel = grpc.insecure_channel(bank_server_endpoint)
        self._bstub = BankStub(self._bank_channel)

        self._balance = self._bstub.balance(
                        balance_request(wallet_key = self._wallet_key)).balance_value


    def price(self, request: price_request, context) -> price_response:
        return price_response(price_value = self._product_value)

    def sale(self, request: sale_request, context) -> sale_response:
        transaction_key = request.transaction_key
        response = self._bstub.transfer(transfer_request(value = self._product_value, 
                        wallet_key = self._wallet_key, transaction_key = transaction_key))

        if response.status >= 0:
            self._balance += self._product_value
            return sale_response(status = response.status)
        else:
            return sale_response(status = -9)

    def end_of_work_store(self, request: end_of_work_store_request, context) -> end_of_work_store_response:
        
        self._stop_event.set()   
        self._bank_channel.close()
        
        return end_of_work_store_response(status = self._balance)

def serve():
    product_value = sys.argv[1]
    endpoint = sys.argv[2]
    wallet_key = sys.argv[3]
    bank_server_endpoint = sys.argv[4]

    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_StoreServicer_to_server(StoreServer(stop_event, product_value, wallet_key, bank_server_endpoint), server)
    server.add_insecure_port("0.0.0.0:{}".format(endpoint))
    
    server.start()
    stop_event.wait()
    server.stop()

if __name__ == '__main__':
    serve()
    