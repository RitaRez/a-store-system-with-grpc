import threading, re, grpc

from sys import argv
from secrets import token_bytes
from concurrent import futures

from bank_pb2_grpc import *
from bank_pb2 import *


class BankServer (BankServicer):
    clients = {}
    transactions = {}

    def __init__(self, stop_event, db_filename):
        self._db_filename = db_filename
        self._stop_event = stop_event
 
        self.read_database()

    def read_database(self) -> None:
        try:
            f = open(self._db_filename, "r")
            for line in f:
                wallet = line.split(" ")
                wallet_key = wallet[0]
                wallet_value = re.sub("\n", "", wallet[1])
                self.clients[wallet_key] = int(wallet_value) 
            f.close()

        except FileNotFoundError:
            print("Wrong file or filepath")

    def save_changes(self) -> None:
        try:
            f = open(self._db_filename, "w")
            for key, value in self.clients.items():
                f.write('{} {}\n'.format(key, value)) 
            f.close()
        except FileNotFoundError:   
            print("Wrong file or filepath")

    def balance(self, request: balance_request, context) -> balance_respose:
        wallet_key = request.wallet_key

        if wallet_key in self.clients:
            balance = self.clients[wallet_key]
        else:
            balance = -1
        
        return balance_respose(balance_value = balance)

    def payment(self, request: payment_request, context) -> payment_respose:
        
        wallet_key = request.wallet_key
        value = request.value
        transaction_key = token_bytes(32)

        if wallet_key not in self.clients:
            status = -1

        elif self.clients[wallet_key] < value:
            status = -2

        else:
            status = 0
            self.clients[wallet_key] -= value
            self.transactions[transaction_key] = value

        return payment_respose(status = status, transaction_key = transaction_key)

    def transfer(self, request: transfer_request, context) -> transfer_respose:

        value = request.value
        transaction_key = request.transaction_key
        wallet_key = request.wallet_key

        if wallet_key not in self.clients:
            status = -1
            
        elif transaction_key not in self.transactions:
            status = -2

        elif self.transactions[transaction_key] != value:
            status = -3

        else:
            self.transactions.pop(transaction_key)
            self.clients[wallet_key] += value
            status = self.clients[wallet_key]

        return transfer_respose(status = status)

    def end_of_work(self, request: end_of_work_request, context) -> end_of_work_respose:

        self.save_changes()
        status = len(self.clients)

        self._stop_event.set()
        return end_of_work_respose(status = status)


def serve():
    endpoint = argv[1]
    db_filename = argv[2]

    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BankServicer_to_server(BankServer(stop_event, db_filename), server)
    server.add_insecure_port("0.0.0.0:{}".format(endpoint))
    
    server.start()
    stop_event.wait()
    server.stop()

if __name__ == '__main__':
    serve()
    