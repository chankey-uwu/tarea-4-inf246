from threading import *
import time
import random
import math
from lobby import Lobby
import jugador
from partida import Partida

lobby = Lobby()
estandar = Partida(15,7,7)
versus = Partida(2,3,4)
rapida = Partida(10,6,8)
navidad = Partida(12,5,10)

for i in range(5):
    j = jugador.jugador(i + 1,lobby)
    j.start()