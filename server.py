import socket
from _thread import *
import sys
from helpers import sendPos, readPos

server = "192.168.0.177"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(10)
print("Waiting for a connection")

pos = [(0, 0), (200, 200)]
playersConnected = 0

def threaded_client(conn, player):
    conn.send(str.encode(sendPos(pos[player][0], pos[player][1])))
    reply=''
    while True:
        try:
            data = readPos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("disconnected")
                break
            else:
                if player == 0:
                    reply = pos[1]
                else:
                    reply = pos[0]
                    
            conn.sendall(str.encode(sendPos(reply[0], reply[1])))
        except error as e:
            print(e)
            break
    print("lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("connected to", addr)
    start_new_thread(threaded_client, (conn, playersConnected))
    playersConnected += 1