from threading import *
from queue import *
from datetime import datetime
from registros import *

class Lobby():
    def __init__(self, partidas):
        self.partidas = partidas
        self.locks = [Lock(),Lock(),Lock(),Lock()]
    
    def llegada(self, jugador):
        partida = jugador.getPartida()
        player_id = jugador.getId()
        ti = datetime.now()
        self.locks[partida].acquire()
        self.partidas[partida].enqueue(jugador)
        tf = datetime.now()
        reg_lobby(player_id, str(ti), partida, str(tf))
        self.locks[partida].release()
        self.partidas[partida].enqueued(jugador)
