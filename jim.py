import argparse
import json



def f_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default='7777')
    parser.add_argument('-a', '--address', default='127.0.0.1')
    return parser.parse_args()

def f_decode(encodet_data):
    result = json.loads(encodet_data.decode('utf-8'))
    return result

def f_encode(decodet_data):
    message = decodet_data
    jmessage = json.dumps(message)
    bjmessage = jmessage.encode('utf-8')
    return bjmessage

def f_check_message():
    pass