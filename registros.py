lobby_file = open("registros/Lobby.txt","w",encoding='utf-8')
estandar_file = open("registros/PartidaEstándar.txt","w")
versus_file = open("registros/PartidaVersus.txt","w")
rapida_file = open("registros/PartidaRápida.txt","w")
navidad_file = open("registros/PartidaEspecialNavidad.txt","w")
salida_file = open("registros/Salida.txt","w")

def conv_partida(partida):
    if partida == 0:
        return "Partida Estándar"
    elif partida == 1:
        return "Partida Versus"
    elif partida == 2:
        return "Partida Rápida"
    elif partida == 3:
        return "Partida Especial Navidad"
    
def conv_hora(hora):
    hora = hora.split(" ")[1]
    return hora

def reg_lobby(player_id, hora_ingreso, partida, hora_salida):
    lobby_file.write("Jugador{}, {}, {}, {}\n".format(player_id,conv_hora(hora_ingreso),conv_partida(partida),conv_hora(hora_salida)))

def reg_partida(player_id, hora_ingreso, hora_salida, partida):    
    if partida == 0:
        estandar_file.write("Jugador{}, {}, {}\n".format(player_id,conv_hora(hora_ingreso),conv_hora(hora_salida)))
        
    elif partida == 1:
        versus_file.write("Jugador{}, {}, {}\n".format(player_id,conv_hora(hora_ingreso),conv_hora(hora_salida)))
        
    elif partida == 2:
        rapida_file.write("Jugador{}, {}, {}\n".format(player_id,conv_hora(hora_ingreso),conv_hora(hora_salida)))

    elif partida == 3: 
        navidad_file.write("Jugador{}, {}, {}\n".format(player_id,conv_hora(hora_ingreso),conv_hora(hora_salida)))  

def reg_salida(player_id, hora):
    salida_file.write("Jugador{}, {}\n".format(player_id,conv_hora(hora)))
    
def cerrar():
    lobby_file.close()
    estandar_file.close()
    versus_file.close()
    rapida_file.close()
    navidad_file.close()
    salida_file.close()