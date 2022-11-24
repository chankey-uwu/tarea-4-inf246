import time

class Partida():
    def __init__(self, game_capacity, duration, queue_capacity):
        self.game_capacity = game_capacity
        self.duration = duration
        self.queue_capacity = queue_capacity
        self.players = list()
        self.queue = list()
        self.in_game = False
    
    def enqueue(self, jugador):
        if len(self.queue) < self.queue_capacity:
            self.queue.append(jugador)
            return True
        else:
            return False
        
    def start_game(self):
        self.in_game = True
        time.sleep(7)
        self.in_game = False
