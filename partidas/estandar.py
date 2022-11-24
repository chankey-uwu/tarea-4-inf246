from threading import *
import time

part_est_activa = False

def partida_estandar(player_id):
    if(part_est_activa == False):
        part_est_activa = True
