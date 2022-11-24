from threading import *
import time
import random
import math
from lobby import Lobby
import jugador

lobby = Lobby()

for i in range(5):
    j = jugador.jugador(i + 1,lobby)
    j.start()