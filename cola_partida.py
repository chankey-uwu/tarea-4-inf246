from datetime import datetime
from threading import *
from registros import *

class cola_partida():

    #Constructor
    # game_id: int, tipo de juego
    # queue_capacity: int, capacidad de la cola
    # game: objeto 'Partida'
    def __init__(self, game_id, queue_capacity, game):
        self.game_id = game_id
        self.queue_capacity = queue_capacity
        self.game = game
        self.queue_quantity = 0
        self.lock = Lock()
        self.semaphore = Semaphore()
        self.fullQueue = False
        self.event_leave_queue = Event()

    # Retorna True si la cola está llena, False si no
    def isFull(self):
        return self.fullQueue
    
    # player: objeto 'jugador'
    # Deja al jugador en la cola de la partida
    def enqueue(self, player):
        self.lock.acquire()
        ti = datetime.now()
        self.queue_quantity += 1
        if self.queue_capacity == self.queue_quantity:
            self.fullQueue = True
        self.lock.release()
        self.goToGame(player, ti)
    
    # player: objeto 'jugador'
    # ti: tiempo de entrada
    # Si la partida se está jugando, espera a que termine
    # Cuando la partida no se está jugando, player juega (entra a) una partida
    def goToGame(self, player, ti):
        self.semaphore.acquire()
        if self.game.isPartida():
            self.game.waitPartida()
        self.queue_quantity -= 1
        self.fullQueue = False
        self.event_leave_queue.set()
        self.semaphore.release()
        self.game.play(player, ti)