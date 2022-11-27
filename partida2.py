import time
from datetime import datetime
from threading import *
from registros import *

class Partida():
    def __init__(self, game_id, queue_capacity):
        self.game_id = game_id
        self.queue_capacity = queue_capacity
        self.sem_enqueue = Semaphore(self.queue_capacity)
        self.queue = list()

    def enqueue(self, jugador):
        self.sem_enqueue.acquire()
