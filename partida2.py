import time
from datetime import datetime
from threading import *
from registros import *

class cola_partida():
    def __init__(self, game_id, queue_capacity):
        self.game_id = game_id
        self.queue_capacity = queue_capacity
        self.queue_quantity = 0
        self.lock = Lock()
        self.fullQueue = False

    def isFull(self):
        return self.fullQueue
    
    def enqueue(self, player):
        self.lock.acquire()
        self.queue_quantity += 1
        if self.queue_capacity == self.queue_quantity:
            self.fullQueue = True