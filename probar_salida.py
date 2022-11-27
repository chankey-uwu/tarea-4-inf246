from partida import Partida
from datetime import datetime
from threading import *
from registros import *
from random import randint
import time

class jugador (Thread):
    def __init__(self, player_id, partida):
        super().__init__()
        self.player_id = player_id
        self.partida = partida

    def waitP(self, event):
        event.wait()
    
    def getId(self):
        return self.player_id

    def run(self):
        self.partida.play(self, datetime.now())
        pass

versus = Partida(1, 2, 3)
j1 = jugador(1, versus)
j1.start()
time.sleep(1)
j2 = jugador(2, versus)
j2.start()


