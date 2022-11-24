from threading import *
from lobby import Lobby
from partida import Partida
import jugador

estandar = Partida(1, 15, 7, 7)
versus = Partida(2, 2, 3, 4)
rapida = Partida(3, 10, 6, 8)
navidad = Partida(4, 12, 5, 10)
partidas = [estandar, versus, rapida, navidad]
lobby = Lobby(partidas)

for i in range(30):
    j = jugador.jugador(i + 1,lobby)
    j.start()