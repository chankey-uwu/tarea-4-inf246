from threading import *
import time
import random
import math
import lobby
import jugador

jugadores = list()
for i in range(5):
    j = jugador.jugador(i,random.randint(1,4))
    jugadores.append(j)
    j.run()

