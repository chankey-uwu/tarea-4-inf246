from threading import *
from lobby import Lobby
from cola_partida import *
from partida import *
import random
import jugador

q_of_games = [0,0,0,0] # Cantidad de juegos
max_game = [15,2,10,12] # Máximos jugadores por tipo de juego
sobras = [0,0,0,0] # Jugadores sobrantes por juego (no hay suficientes para iniciar una partida)
seleccion_partidas = list()
i = 0
while 120 > i:
    x = random.randint(0,3)
    sobras[x] += 1
    seleccion_partidas.append(x)
    if sobras[x] == max_game[x]:
        sobras[x] = 0
        q_of_games[x] += 1
    i += 1
estandar = cola_partida(0, 7, Partida(0, 15, 7, q_of_games[0], sobras[0]))
versus = cola_partida(1, 4, Partida(1, 2, 3, q_of_games[1], sobras[1]))
rapida = cola_partida(2, 8, Partida(2, 10, 6, q_of_games[2], sobras[2]))
navidad = cola_partida(3, 10, Partida(3, 12, 5, q_of_games[3], sobras[3]))
partidas = [estandar, versus, rapida, navidad]
lobby = Lobby(partidas)

for i in range(120):
    p = seleccion_partidas[i]
    j = jugador.jugador(i + 1,lobby, p)
    j.start()