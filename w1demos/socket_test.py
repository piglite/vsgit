import socket
from urllib.parse import quote_plus
req_text='''
    GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n
    User-Agent: socket_test.py(vipcode)\r\n
    Connection:close \r\n
    \r\n
 '''

def geocode(address):
    s = socket.socket()
    s.connect(('maps.googleapis.com',80))
    req = req_text.format(quote_plus(address))
    s.sendall(req.encode('ascii'))
    rep = b''
    while True:
        m = s.recv(4096)
        if not m:
            break
        else:
            rep+=m
    print(rep.decode('utf-8'))

if __name__=='__main__':
    geocode('207 N. Definace St, Archbold, OH')
    