from threading import *
from queue import *
import time
import random
import math
from partidas import estandar

class Lobby():
    def __init__(self):
        self.estandar = list()
        self.versus = list()
        self.rapida = list()
        self.navidad = list()
        self.lock = Lock()
    
    def llegada(self, j):
        cola_temp = None
        if j.getPartida() == 1:
            cola_temp = self.estandar
        elif j.getPartida() == 2:
            cola_temp = self.versus
        elif j.getPartida() == 3:
            cola_temp = self.rapida
        elif j.getPartida() == 4:
            cola_temp = self.navidad

        cola_temp.append(j.getId())
        ti = time.time()
        print(cola_temp)
        self.lock.acquire()
        time.sleep(1)
        print("Jugador {} a partida {}".format(j.getId(), j.getPartida()))
        print(time.time() - ti)
        cola_temp.pop(0)
        print(cola_temp)
        self.lock.release()




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
