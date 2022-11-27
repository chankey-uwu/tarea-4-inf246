import time
from datetime import datetime
from threading import *
from registros import *

class cola_partida():
    def __init__(self, game_id, queue_capacity, game): #pasarle a game el partidas[partida]
        self.game_id = game_id
        self.queue_capacity = queue_capacity
        self.game = game
        self.queue_quantity = 0
        self.lock = Lock()
        self.semaphore = Semaphore()
        self.fullQueue = False
        self.event_leave_queue = Event()

    def isFull(self):
        return self.fullQueue
    
    def enqueue(self, player):
        self.lock.acquire()
        ti = datetime.now()
        self.queue_quantity += 1
        if self.queue_capacity == self.queue_quantity:
            self.fullQueue = True
        self.lock.release()
        self.goToGame(player, ti)
    
    def goToGame(self, player, ti):
        self.semaphore.acquire()
        if self.game.isPartida():
            self.game.waitPartida()
        self.queue_quantity -= 1
        self.fullQueue = False
        self.event_leave_queue.set()
        self.semaphore.release()
        self.game.play(player, ti)
