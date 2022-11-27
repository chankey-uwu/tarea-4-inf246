import time
from datetime import datetime
from threading import *
from registros import *

class Partida():
    def __init__(self, game_id, game_capacity, duration):
        self.game_id = game_id
        self.game_capacity = game_capacity
        self.duration = duration
        self.quantity = 0
        self.semaphore = Semaphore()
        self.full = False
        self.in_game = False
        
    def isPartida(self):
        return self.in_game

    def isFull(self):
        return self.full
    
    def play(self, player):
        self.semaphore.acquire()
        if         