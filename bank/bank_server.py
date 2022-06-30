import logging, asyncio
from sys import argv
from grpc import aio
from secrets import token_bytes

from bank_pb2_grpc import *
from bank_pb2 import *


class BankServer (BankServicer):
    
    def __init__(self, db_filename):
        self.db_filename = db_filename

    def search_for_wallet_key(self, wallet_key):

        f = open(self.db_filename, "r")

        balance = -1
        for line in f:
            wallet = line.split(" ")
            if wallet[0] == wallet_key:
                balance = int(wallet[1])
                break
        f.close()

        return balance

    async def balance(self, request: balance_request, context) -> balance_respose:
        wallet_key = request.wallet_key
        balance = self.search_for_wallet_key(wallet_key)
        
        return balance_respose(balance_value = balance)

    async def payment(self, request: payment_request, context) -> payment_respose:
        return payment_respose(status = 0, auth_token = token_bytes(32))


async def serve() -> None:
    db_filename = argv[1]
    endpoint = argv[2]

    server = aio.server()
    add_BankServicer_to_server(BankServer(db_filename), server)
    server.add_insecure_port(endpoint)
    logging.info("Starting server on %s", endpoint)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
    