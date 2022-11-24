from threading import *
import time
import random
import math
import lobby
import jugador

lobby = lobby.lobby_class()
for i in range(5):
    j = jugador.jugador(i)
    lobby.llegada(i,j.partida)
    j.run()


