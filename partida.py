import time
from datetime import datetime
from threading import *
from registros import *

class Partida():
    def __init__(self, game_id, game_capacity, duration, q, s):
        self.game_id = game_id
        self.game_capacity = game_capacity
        self.duration = duration
        self.q = q
        self.s = s
        self.games_started = 0
        self.quantity = 0
        self.semaphore = Semaphore()
        self.event_game_start = Event()
        self.event_game_end = Event()
        
    def isPartida(self):
        return self.event_game_start.is_set()
    
    def waitPartida(self):
        self.event_game_end.wait()

    def play(self, player, ti):
        self.semaphore.acquire()
        self.quantity += 1
        if (self.game_capacity == self.quantity) or (self.games_started == self.q and self.quantity == self.s):
            self.event_game_start.set()
            time.sleep(0.00001)
            reg_partida(player.getId(),str(ti),str(datetime.now()),self.game_id)
            self.games_started += 1
            time.sleep(self.duration)
            self.event_game_end.set()
            time.sleep(0.00001)
            reg_salida(player.getId(),str(datetime.now()))
            self.event_game_start.clear()
            self.event_game_end.clear()
            self.quantity = 0
            self.semaphore.release()
        else:
            self.semaphore.release()
            self.event_game_start.wait()
            reg_partida(player.getId(),str(ti),str(datetime.now()),self.game_id)
            self.event_game_end.wait()
            reg_salida(player.getId(),str(datetime.now()))