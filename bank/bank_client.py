import logging, asyncio
from sys import argv
from grpc import aio
from secrets import token_bytes

from bank_pb2_grpc import *
from bank_pb2 import *

if __name__ == '__main__':

    channel = grpc.insecure_channel('localhost:8888')
    bs = BankStub(channel)
    awnser = bs.balance(balance_request(wallet_key = "rita"))
    awnser = bs.balance(balance_request(wallet_key = "luiz"))

    print(awnser.balance_value)