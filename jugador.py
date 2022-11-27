from threading import *

class jugador (Thread):
    # Constructor
    # player_id: int, id del jugador
    # lobby: objeto 'Lobby'
    # partida: objeto 'Partida'
    def __init__(self, player_id, lobby, partida):
        super().__init__()
        self.lobby = lobby
        self.player_id = player_id
        self.partida = partida

    # get del id del jugador
    def getId(self):
        return self.player_id
    
    # get de objeto 'Partida'
    def getPartida(self):
        return self.partida

    # Encola al jugador en la cola de la partida si es que hay espacio en la cola
    def run(self):
        self.lobby.llegada(self)
        pass