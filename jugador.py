from threading import *

class jugador (Thread):
    def __init__(self, player_id, lobby, partida):
        super().__init__()
        self.lobby = lobby
        self.player_id = player_id
        self.partida = partida

    def waitEvent(self, event):
        event.wait()        
    
    def getId(self):
        return self.player_id
    
    def getPartida(self):
        return self.partida

    def run(self):
        self.lobby.llegada(self)
        pass