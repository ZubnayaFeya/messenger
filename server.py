import socket
import json
#from time import time
#import argparse
import jim
from type_msg import *


class CServer():
    def __init__(self, queue=25, timeout=0):
        self.args = jim.f_parser()
        self.queue = queue
        self.timeout = timeout
        self.sock = None

    def sock_serv(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.args.address, int(self.args.port)))
        sock.listen(self.queue)
        #sock.settimeout(self.timeout)
        self.sock = sock

    def recv_message(self):
        self.client_sock, addr = self.sock.accept()
        while True:
            print("Получен запрос на соединение от {}".format(str(addr)))
            result = self.client_sock.recv(1024)
            result = jim.f_decode(result)
            return result

    def translate_message(self, recv_message):
        if recv_message['action'] == 'presence':
            return '200'
        #elif recv_message['action'] ==
        else:
            return '400'

    def send_alert(self, code_result):
        #code_result = translate_message
        data = f_alert(code_result, code[code_result])
        data = json.dumps(data).encode('utf-8')
        self.client_sock.send(data)

serv = CServer()
serv.sock_serv()
a = serv.recv_message()
b = serv.translate_message(a)
serv.send_alert(b)
serv.client_sock.close()
#    client_sock.close()