# Tarea 4

## Partidas

- Partida Estándar: capacidad 15 jugadores, duración 7 segundos, cola 7 jugadores 
- Partida Versus: capacidad 2 jugadores, duración 3 segundos, cola 4 jugadores 
- Partida Rápida: capacidad 10 jugadores, duración 6 segundos, cola 8 jugadores 
- Partida Especial Navidad: capacidad 12 jugadores, duración 5 segundos, cola 10 jugadores 

## Organización

### Inicio y programa general
Inicia programa, jugadores (hebras) entran al lobby y se les asigna una partida de forma aleatoria por orden de llegada, y luego se irá del juego.

### Jugador en la partida
Jugador verifica si la cola de la partida que va está llena o no, si hay espacio, jugador entra a la cola de la partida. 
Si no hay, queda esperando en el lobby que se termine la partida, jugadores en espera en el lobby a que se vacíe una cola entran a su respectiva cola de partida en orden de llegada a dicha cola.

### Partida
Partida sólo empieza si se llena la cola, una vez empieza, cola se vacía y empieza la partida (nuevos jugadores pueden entrar a la cola mientras la partida está en curso). Al terminar la partida jugadores abandonan el juego.

## Registros

Listo

## Problemas a solucionar

Hebras en espera de algo