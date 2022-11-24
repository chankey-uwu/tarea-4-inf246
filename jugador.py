from threading import *
import lobby

class jugador (Thread):
    def __init__(self, player_id, partida):
        self.player_id = player_id
        self.partida = partida

    def run(self):
        lobby.lobby_enqueue(self.player_id,self.partida)
        pass