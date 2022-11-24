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
        """
        event = Event()
        jugador.waitEvent(event)
        while self.partidas[partida].enqueue(jugador) == False:
            time.sleep(random.randint(0,5))
        """
        cola_temp.pop(0)
        self.locks[partida].release()
        tf = datetime.now()
        reg_lobby(player_id, str(ti), partida, str(tf))
        #self.partidas[partida].enqueued(jugador)

    def wait_game(self, event, game):
        print("uwu")
