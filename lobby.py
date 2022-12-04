from threading import *
from queue import *
from datetime import datetime
from registros import *

class Lobby():
    # Constructor
    # partidas: lista de objetos 'Partida'
    def __init__(self, partidas):
        self.partidas = partidas
        self.locks = [Lock(),Lock(),Lock(),Lock()]
        self.queues = [[],[],[],[]]
    
    # jugador: objeto 'jugador'
    # Encola al jugador en la cola de la partida si es que hay espacio en la cola
    def llegada(self, jugador):
        ti = datetime.now()
        partida = jugador.getPartida()
        player_id = jugador.getId()
        self.queues[partida].append(player_id)
    
        while self.queues[partida][0] != player_id:
            self.partidas[partida].event_leave_queue.wait()

        self.locks[partida].acquire()
        
        if self.partidas[partida].isFull():
            self.partidas[partida].event_leave_queue.wait()
            self.partidas[partida].event_leave_queue.clear()
            
        tf = datetime.now()
        reg_lobby(player_id, str(ti), partida, str(tf))
        self.queues[partida].pop(0)
        self.locks[partida].release()
        self.partidas[partida].enqueue(jugador)
