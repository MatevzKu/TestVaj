# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 08:05:49 2017

@author: matev
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 21:15:51 2017

@author: Matevz
"""

import socket as socket
from random import random as rn

def normalize_line_endings(s):
    r'''Convert string containing various line endings like \n, \r or \r\n,
    to uniform \n.'''

    return ''.join((line + '\n') for line in s.splitlines())


MAX_PACKET = 32768

def recv_all(sock):
    r'''Receive everything from `sock`, until timeout occurs, meaning sender
    is exhausted, return result as string.'''

    # dirty hack to simplify this stuff - you should really use zero timeout,
    # deal with async socket and implement finite automata to handle incoming data

    prev_timeout = sock.gettimeout()
    try:
        sock.settimeout(0.01)

        rdata = []
        while True:
            try:
                rdata.append(sock.recv(MAX_PACKET))
            except socket.timeout:
                return ''.join(rdata)

        # unreachable
    finally:
        sock.settimeout(prev_timeout)

host = socket.gethostname()
port = 8080


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
counter=0

while True:
    client_sock, client_addr = s.accept()
    print(client_sock)
    print(client_addr)
    #request = normalize_line_endings(recv_all(client_sock)) # hack again
    #request = recv_all(client_sock)
    #print (request)
    response_body = [        
        '{"temp":' + str(80.0*rn()) + ',"hum":' + str(60.0*rn()) + ',"pres":' + str(80.0*rn()) + '}'
    ]

    response_body_raw = ''.join(response_body)

    # Clearly state that connection will be closed after this response,
    # and specify length of response body
    response_headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'text/html; encoding=utf8',
        'Content-Length': len(response_body_raw),
        'Connection': 'close',
    }

    response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in \
                                            response_headers.items())

    # Reply as HTTP/1.1 server, saying "HTTP OK" (code 200).
    response_proto = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK\n' # this can be random

    # sending all this stuff
#    client_sock.send('%s %s %s' % (response_proto, response_status, \
#                                                    response_status_text))
    client_sock.send(str.encode(response_proto))
    client_sock.send(str.encode(response_status))
    client_sock.send(str.encode(response_status_text))
    client_sock.send(str.encode(response_headers_raw))
    client_sock.send(str.encode('\n')) # to separate headers from body
    client_sock.send(str.encode(response_body_raw))

    # and closing connection, as we stated before
    client_sock.close()

