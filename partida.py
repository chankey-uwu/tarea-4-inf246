import time
from datetime import datetime
from threading import *
from registros import *

class Partida():
    def __init__(self, game_id, game_capacity, duration, queue_capacity):
        self.game_id = game_id
        self.game_capacity = game_capacity
        self.duration = duration
        self.queue_capacity = queue_capacity
        self.semaphore = BoundedSemaphore(queue_capacity)
        self.players = list()
        self.queue = list()
        self.semaphore_enqueue = Semaphore()
        self.in_game = False
        self.evento_cola = Event()
        self.evento_partida = Event()

    def enqueue(self, jugador):
        self.semaphore_enqueue.acquire()
        if len(self.queue) < self.queue_capacity:
            self.queue.append(jugador)
        else:
            self.evento_cola.wait()
            self.queue.append(jugador)
            self.evento_cola.clear()
        self.semaphore_enqueue.release()
            
    def enqueued(self, jugador):
        ti = datetime.now()
        print("ALGUIEN SE ENCOLÓ EN {}".format(self.game_id))
        self.semaphore.acquire()
        if self.in_game == False and len(self.queue) == self.queue_capacity:
            for p in self.queue:
                self.players.append(p)
            self.start_game()
            self.semaphore.release()
        elif self.in_game == False and len(self.queue) < self.queue_capacity:
            self.evento_partida.wait()
            self.semaphore.release()
        elif self.in_game == True and len(self.players) == self.game_capacity:
            self.evento_partida.wait()
            self.semaphore.release()
        tf = datetime.now()
        reg_partida(jugador.getId(),str(ti),str(tf),self.game_id)
            
    def getType(self):
        return self.duration

    def start_game(self):
        self.in_game = True
        self.evento_cola.set()
        time.sleep(7)
        self.in_game = False
        self.evento_partida.set()

    def play(self, jugador):
        self.evento_partida.wait()
        t = datetime.now()
        reg_salida(jugador.getId(),str(t))
