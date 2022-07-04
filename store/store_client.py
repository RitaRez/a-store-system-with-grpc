import sys
from secrets import token_bytes

sys.path.append('./bank')
from bank_pb2_grpc import *
from bank_pb2 import *
from store_pb2_grpc import *
from store_pb2 import *

def get_price_and_balance(sstub, bstub, wallet_key):
    store_price = sstub.price(price_request()).price_value
    client_balance = bstub.balance(balance_request(wallet_key = wallet_key)).balance_value
    
    print("{} {}".format(store_price, client_balance))
    return store_price

def make_sale(bstub, sstub, wallet_key, store_price):
            
    preq = payment_request(wallet_key = wallet_key, value = store_price)    
    pres = bstub.payment(preq)
    print(pres.status)
    
    if pres.status >= 0:
        sreq = sale_request(transaction_key = pres.transaction_key)
        sres = sstub.sale(sreq)
        print(sres.status)

   
def run(wallet_key, bank_server_endpoint, store_server_endpoint):

    bank_channel = grpc.insecure_channel(bank_server_endpoint)
    bstub = BankStub(bank_channel)
    store_channel = grpc.insecure_channel(store_server_endpoint)
    sstub = StoreStub(store_channel)
    
    store_price = 0    
    while True:
        command = input() 
        commands = command.split(' ')
        
        if commands[0] == 'P':
            store_price = get_price_and_balance(sstub, bstub, wallet_key)

        elif commands[0] == 'C':
            make_sale(bstub, sstub, wallet_key, store_price)

        elif commands[0] == 'T':
            bres = bstub.end_of_work(end_of_work_request())
            sres = sstub.end_of_work_store(end_of_work_store_request())
            print(sres.status)
            print(bres.status)
            break
            
        else:
            pass

    bank_channel.close()
    store_channel.close()


if __name__ == '__main__':

    wallet_key = sys.argv[1]
    bank_server_endpoint = sys.argv[2]
    store_server_endpoint = sys.argv[3]

    run(wallet_key, bank_server_endpoint, store_server_endpoint)