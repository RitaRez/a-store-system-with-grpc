import os    # necessário para o getpid
import rpyc

def rpyc_call():

    # Antes de mais nada, o cliente tem que identificar 
    #   e se conectar ao servidor
    conn = rpyc.connect('localhost',8888)

    my_pid = os.getpid()
    
    # Primeira chamada. Todo método fica disponível em conn.root.
    # Notem que em RPyC não é preciso chamar explicitamente o código de
    #   serialização. RPyC cuida disso internamente.
    myval = conn.root.say_hello(my_pid)
    print("RPyC client received: ", myval)

    # Segunda chamada. Feita da mesma forma.
    myval = conn.root.say_hello_again(my_pid)
    print("RPyC client received: ", myval)

    # Ao final, o cliente pode explicitamente se desconectar do servidor
    conn.close()

if __name__ == '__main__':
    rpyc_call()
