from threading import *
from queue import *
import time
import random
import math
from partidas import estandar
import jugador

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


