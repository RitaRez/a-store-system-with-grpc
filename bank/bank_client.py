from sys import argv
from grpc import aio
from secrets import token_bytes

from bank_pb2_grpc import *
from bank_pb2 import *

def get_balance(bstub, wallet_key):
    breq = balance_request(wallet_key = wallet_key)
    
    return bstub.balance(breq)

def make_payment(bstub, commands, transactions, wallet_key):
    
    value = int(commands[1])
    preq = payment_request(wallet_key = wallet_key, value = value)    
    
    return bstub.payment(preq)
    
def save_payment(awnser, transactions):
    if awnser.status >= 0:
        payment_id = len(transactions) + 1
        transactions[payment_id] = awnser.transaction_key
        return payment_id
    
    else:
        return awnser.status

def make_transfer(bstub, commands, transactions, wallet_key):

    value = int(commands[1]); op = int(commands[2]); destination_key = commands[3]

    if op in transactions:
        tr = transfer_request(value = value, wallet_key = destination_key, transaction_key = transactions[op])
        response = bstub.transfer(tr)
        return response.status
    else:
        return -9

def run(wallet_key, endpoint):

    channel = grpc.insecure_channel(endpoint)
    bstub = BankStub(channel)
    
    transactions = {}
    
    while True:
        command = input() 
        commands = command.split(' ')
        
        if   commands[0] == 'S':
            response = get_balance(bstub, wallet_key)
            print(response.balance_value)

        elif commands[0] == 'O':
            response = make_payment(bstub, commands, transactions, wallet_key)
            awnser = save_payment(response, transactions)
            print(awnser)
            
        elif commands[0] == 'X':
            awnser = make_transfer(bstub, commands, transactions, wallet_key)  
            print(awnser)

        elif commands[0] == 'F':
            response = bstub.end_of_work(end_of_work_request())
            print(response.status)
            break
            
        else:
            pass

    channel.close()


if __name__ == '__main__':

    wallet_key = argv[1]
    endpoint = argv[2]

    run(wallet_key, endpoint)