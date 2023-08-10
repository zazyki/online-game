import socket
from _thread import *
import pickle
from helpers import sendPos, readPos
from player import Player

server = "192.168.0.177"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(10)
print("Waiting for a connection")

players = [Player(100 ,100 , 50, 50, (0,0,0)), Player(500 ,500 , 50, 50, (0,0,0))]
playersConnected = 0

def threaded_client(conn, player):
    print(player)
    conn.send(pickle.dumps(players[player]))
    reply=''
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("disconnected")
                break
            else:
                if player == 0:
                    reply = players[1]
                else:
                    reply = players[0]
                    
            conn.sendall(pickle.dumps(reply))
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