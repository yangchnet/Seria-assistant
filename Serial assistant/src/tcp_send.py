from socket import *
import time
import threading

def send(send_str):
    HOST = '183.230.40.34'
    PORT = 80
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpClisock = socket(AF_INET, SOCK_STREAM)
    tcpClisock.connect(ADDR)
    data = '''
    POST /devices/525711692/datapoints?type=3 HTTP/1.1 
    api-key:OhZNJp=6grNUNUF=ND18Z7hfe8k= 
    Host:api.heclouds.com 
    Content-Length:59
    
    {"datastreams":[{"id":"temp","datapoints":[{"value":50}]}]}'''

    tcpClisock.send(send_str)
    tcpClisock.close()