import socket
from _thread import *
import pickle
from player import Player
from pygame.sprite import Group
from bullet import Bullet

class Server():

    def __init__(self, server, port):
        self.server = server
        self.port = port

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((self.server, self.port))
        except socket.error as e:
            print(e)
        s.listen(10)
        print("Waiting for a connection")

        self.players = [Player(100 ,100 , 50, 50, (0,0,0)), Player(500 ,500 , 50, 50, (0,0,0)),Player(200 ,200 , 50, 50, (0,0,0)), Player(300 ,300 , 50, 50, (0,0,0)), Group()]
        self.playersConnected = 0      

        while True:
            conn, addr = s.accept()
            print("connected to", addr)
            start_new_thread(self.threaded_client, (conn, self.playersConnected))
            self.playersConnected += 1

    def threaded_client(self, conn, player):
        print(player)
        conn.send(pickle.dumps(self.players[player]))
        reply=''
        while True:
            try:
                data = pickle.loads(conn.recv(16384))
                self.players[player] = data

                for i in self.players[player].bullets:
                    self.players[4].add(Bullet(i[0],i[1],i[2]))
                for b in self.players[4]:
                    b.update()    

                if not data:
                    print("disconnected")
                    break
                else:
                    playersCopy = list(self.players)
                    del playersCopy[player]
                    reply = playersCopy
                        
                conn.sendall(pickle.dumps(reply))
            except error as e:
                print(e)
                break
        print("lost connection")
        conn.close()

    def get_playersConnected(self):
        return self.playersConnected
        
#server = "192.168.0.177"
#port = 80










