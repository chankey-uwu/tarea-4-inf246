from threading import *
from lobby import Lobby
from cola_partida import cola_partida
import jugador

estandar = cola_partida(0, 15, 7, 7)
versus = cola_partida(1, 2, 3, 4)
rapida = cola_partida(2, 10, 6, 8)
navidad = cola_partida(3, 12, 5, 10)
partidas = [estandar, versus, rapida, navidad]
lobby = Lobby(partidas)

for i in range(120):
    j = jugador.jugador(i + 1,lobby)
    j.start()