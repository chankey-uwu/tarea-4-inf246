lobby_file = open("registros/Lobby.txt","w")
estandar_file = open("registros/PartidaEstándar.txt","w")
versus_file = open("registros/PartidaVersus.txt","w")
rapida_file = open("registros/PartidaRápida.txt","w")
navidad_file = open("registros/PartidaEspecialNavidad.txt","w")
salida_file = open("registros/Salida.txt","w")

def conv_partida(partida):
    if partida == 1:
        return "Partida Estándar"
    elif partida == 2:
        return "Partida Versus"
    elif partida == 3:
        return "Partida Rápida"
    elif partida == 4:
        return "Partida Especial Navidad"
    
def conv_hora(hora):
    hora = hora.split(" ")[1]
    return hora

def reg_lobby(player_id, hora_ingreso, partida, hora_salida):
    lobby_file.write("Jugador{}, {}, {}, {}\n".format(player_id,conv_hora(hora_ingreso),conv_partida(partida),conv_hora(hora_salida)))

def reg_estandar(player_id, hora_ingreso, hora_salida): 
    estandar_file.write("Jugador{}, {}, {}, {}\n".format(player_id,conv_hora(hora_ingreso),conv_hora(hora_salida)))

def reg_versus(player_id, hora_ingreso, hora_salida): 
    versus_file.write("Jugador{}, {}, {}, {}\n".format(player_id,conv_hora(hora_ingreso),conv_hora(hora_salida)))

def reg_rapida(player_id, hora_ingreso, hora_salida): 
    rapida_file.write("Jugador{}, {}, {}, {}\n".format(player_id,conv_hora(hora_ingreso),conv_hora(hora_salida)))

def reg_navidad(player_id, hora_ingreso, hora_salida): 
    navidad_file.write("Jugador{}, {}, {}, {}\n".format(player_id,conv_hora(hora_ingreso),conv_hora(hora_salida)))

def reg_salida(player_id, hora):
    salida_file.write("Jugador{}, {}\n".format(player_id,conv_hora(hora)))