from threading import *
import random
import lobby

class jugador (Thread):
    def __init__(self, player_id):
        self.player_id = player_id
        self.partida = random.randint(1,4)

    def getId(self):
        return self.player_id

    def run(self):
        print("Partida del jugador {}: {}".format(self.player_id,self.partida))

        pass