from rpyc.utils import server # para facilitar a escrita do código
import rpyc

# O conjunto de procedimentos oferecidos deve ser colocado em uma classe
class DoStuff(rpyc.Service):

   # Primeiro método: parâmetros self e um inteiro
   # O prefixo exposed_ é obrigatório para mostrar que o método pode
   #   ser acessado pelo cliente.
   # Como estamos usando só um parâmetro, ele pode aparecer dessa forma
   def exposed_say_hello(self, pid):
      print("RPyC server in say_hello, pid =", str(pid))
      return "Hello, %d!" % pid  # O string será enviado para o cliente

   # Segundo método. Usa os mesmos parâmetros, mas nesse caso o código
   #   usa a assinatura correta recomendada por RPyC: duas listas de
   #   argumentos podem ser entregues e processadas.
   def exposed_say_hello_again(self, *args, **kwargs):
      print("RPyC server in say_hello_again, pid =", str(args[0]))
      return "Hello again, %d!" % args[0]

if __name__ == '__main__':
   # No mínimo, o servidor deve receber a classe que contém os
   #   procedimentos oferecidos ao cliente e a identificação do servidor
   #   na rede (endereço IP e porto). Caso seja desejado, existem
   #   parâmetros para incluir um diretório de serviços (registry), 
   #   recursos de autenticação e criptografia, entre outros.
   server.ThreadedServer( 
                          DoStuff,
                          hostname='localhost', port=8888
                       ).start()

# Tipos de servidor disponiveis: 
#        ThreadedServer
#        ForkingServer
#        ThreadPoolServer
#        OneShotServer
#  
