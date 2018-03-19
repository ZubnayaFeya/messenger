import socket
import json
import argparse
#from time import ctime
from type_msg import *
import jim


class CClient():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('localhost', 7777))

    def prepare_data(self):
        type_data = f_presence()
        return type_data

    def send_data(self, data):
        self.sock.send(jim.f_encode(data))

    def recv_data(self):
        result = self.sock.recv(1024)
        return result

    def prepare_resalt(self, result):
        return jim.f_decode(result)

cli = CClient()
prep_d = cli.prepare_data()
cli.send_data(prep_d)
res = cli.recv_data()
print(cli.prepare_resalt(res))
res.self.sock.close()




'''
message = f_presence()
jmessage = json.dumps(message)
bjmessage = jmessage.encode('utf-8')

s = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM, proto = 0)
s.connect(('localhost', 7777))
s.send(bjmessage)

while 1:
    result = s.recv(1024)
    result = result.decode('utf-8')
    result = json.loads(result)


print("Полученый ответ: {}".format(result))
s.close()
'''