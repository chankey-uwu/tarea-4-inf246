from threading import *
import random
import lobby

class jugador (Thread):
    def __init__(self, player_id, lobby):
        super().__init__()
        self.lobby = lobby
        self.player_id = player_id
        self.partida = random.randint(0,3)

    def getId(self):
        return self.player_id
    
    def getPartida(self):
        return self.partida

    def run(self):
        self.lobby.llegada(self)
        pass