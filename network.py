import socket
import pickle

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.177"
        self.port = 80
        self.addr = (self.server, self.port)
        self.rcv = self.connect()

    def getRcv(self):
        return self.rcv

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(16384))
        except:
            pass
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(16384))
        except socket.error as e:
            print(e)

