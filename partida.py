import time
from datetime import datetime
from threading import Lock
from registros import *

class Partida():
    def __init__(self, game_id, game_capacity, duration, queue_capacity):
        self.game_id = game_id
        self.game_capacity = game_capacity
        self.duration = duration
        self.queue_capacity = queue_capacity
        self.players = list()
        self.queue = list()
        self.lock = Lock()
        self.lock_enqueue = Lock()
        self.in_game = False

    def enqueue(self, jugador):
        self.lock_enqueue.acquire()
        if len(self.queue) < self.queue_capacity:
            self.queue.append(jugador)
            self.lock_enqueue.release()
            return True
        else:
            self.lock_enqueue.release()
            return False

    def enqueued(self, jugador):
        ti = datetime.now()
        self.lock.acquire()
        if self.in_game == False and len(self.queue) == self.queue_capacity:
            self.start_game()
        elif self.in_game == False and len(self.queue) < self.queue_capacity:
            while(len(self.enqueue) < self.queue_capacity):
                time.sleep()
            self.start_game()
        elif self.in_game == True and len(self.players) == self.game_capacity:
            while self.in_game:
                time.sleep()
            self.start_game()
        self.lock.release()
        tf = datetime.now()
        reg_partida(jugador.getId(),ti,tf,self.game_id)

            
    def getType(self):
        return self.duration

    def start_game(self):
        self.in_game = True
        time.sleep(7)
        self.in_game = False

    def play(self, jugador):
        print("Uwu")
