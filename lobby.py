from threading import *
from queue import *
import time
import random
from datetime import datetime
from partida import Partida
from registros import *

class Lobby():
    def __init__(self, partidas):
        self.partidas = partidas
        self.partidas_wait = [list(),list(),list(),list()]
        self.locks = [Lock(),Lock(),Lock(),Lock()]
    
    def llegada(self, jugador):
        cola_temp = None
        partida = jugador.getPartida()
        player_id = jugador.getId()
        cola_temp = self.partidas_wait[partida]
        cola_temp.append(player_id)
        ti = datetime.now()
        self.locks[partida].acquire()
        self.partidas[partida].enqueue(jugador)
        cola_temp.pop(0)
        tf = datetime.now()
        reg_lobby(player_id, str(ti), partida, str(tf))
        self.locks[partida].release()
        self.partidas[partida].enqueued(jugador)
