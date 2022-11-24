from threading import *
from queue import *
import time
from datetime import datetime
import random
import math
from partida import Partida
from registros.registros import *

class Lobby():
    def __init__(self):
        self.estandar = list()
        self.versus = list()
        self.rapida = list()
        self.navidad = list()
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock3 = Lock()
        self.lock4 = Lock()
    
    def llegada(self, jugador):
        cola_temp = None
        partida = jugador.getPartida()
        player_id = jugador.getId()
        if partida == 1:
            cola_temp = self.estandar
        elif partida == 2:
            cola_temp = self.versus
        elif partida == 3:
            cola_temp = self.rapida
        elif partida == 4:
            cola_temp = self.navidad

        cola_temp.append(player_id)
        ti = datetime.now()
        self.lockear(partida)
        cola_temp.pop(0)
        tf = datetime.now()
        reg_lobby(player_id, str(ti), partida, str(tf))
        self.deslockear(partida)

    def lockear(self, n):
        if n == 1:
            self.lock1.acquire()
        elif n == 2:
            self.lock2.acquire()
        elif n == 3:
            self.lock3.acquire()
        elif n == 4:
            self.lock4.acquire()
        
    def deslockear(self, n):
        if n == 1:
            self.lock1.release()
        elif n == 2:
            self.lock2.release()
        elif n == 3:
            self.lock3.release()
        elif n == 4:
            self.lock4.release()

"""
cantPlayers = 0
lobby_queue = Queue
lock = Lock
def lobby_enqueue(player_id, partida):
    ti = time.time()
    cantPlayers += 1
    lobby_queue.put(cantPlayers - 1,player_id)
    lock.acquire()
    time.sleep(2)
    print("Jugador {} va a partida {}".format(player_id,partida))
    tf = time.time() - ti
    lock.release()
"""
