'''Simular beneficios de estrategias de juego de un casino. En la ruleta, cada 3000 milisegundos el croupier saca un numeor al azar y los diversos hilos pauestan a ver si ganan.
Todos los hilos empiezan con 1000 euros y la banca con 50000. Cuando lo sjugadores pierden dinero la banca incrementa su dinero.'''

#Se puede jugar a un número concreto. Habrá 4 hilos que eligen números al azar del 1 al 36 (no el 0) y restarán 10 euros de su saldo para apostar a ese número. Si sale su número su saldo se incrementa en 360 euros (36 veces lo apostado).
#Se puede jugar a par/impar. Habrá 4 hilos que eligen al azar si apuestan a que saldrá un número par o un número impar. Siempre restan 10 euros para apostar y si ganan incrementan su saldo en 20 euros.
#Se puede jugar a la «martingala». Habrá 4 hilos que eligen números al azar. Elegirán un número y empezarán restando 10 euros de su saldo para apostar a ese número. Si ganan incrementan su saldo en 360 euros. Si pierden jugarán el doble de su apuesta anterior (es decir, 20, luego 40, luego 80, y así sucesivamente)
#La banca acepta todas las apuestas pero nunca paga más dinero del que tiene.
#Si sale el 0, todo el mundo pierde y la banca se queda con todo el dinero.


import threading
import random
import time

n_hilos = 4
dinero_hilo = 1000
dinero_banca = 50000
tiempo_entre_jugadas = 3    #en segundos

def numero_aleatorio():
    numero = random.randint(1, 36)
    return numero

def par_impar():
    numero = numero_aleatorio()
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'

def apuesta_numero():
    numero = numero_aleatorio()
    return numero

def apuesta_martingala():
    numero = numero_aleatorio()
    apuesta = 10
    while True:
        if numero == apuesta:
            return apuesta
        else:
            apuesta *= 2

def jugar_a_numero():
    global dinero_hilo
    global dinero_banca
    numero = apuesta_numero()
    dinero_hilo -= 10
    dinero_banca += 10
    if numero == numero_aleatorio():
        dinero_hilo += 360
        dinero_banca -= 360
    else:
        pass


def jugar_a_par_impar():
    global dinero_hilo
    global dinero_banca
    par_impar = par_impar()
    dinero_hilo -= 10
    dinero_banca += 10
    if par_impar == par_impar():
        dinero_hilo += 20
        dinero_banca -= 20
    else:
        pass

def jugar_a_martingala():
    global dinero_hilo
    global dinero_banca
    apuesta = apuesta_martingala()
    dinero_hilo -= apuesta
    dinero_banca += apuesta
    if apuesta == numero_aleatorio():
        dinero_hilo += apuesta * 36
        dinero_banca -= apuesta * 36
    else:
        pass

def jugar():
    while True:
        jugar_a_numero()
        jugar_a_par_impar()
        jugar_a_martingala()
        time.sleep(tiempo_entre_jugadas)

def main():
    for i in range(n_hilos):
        t = threading.Thread(target=jugar)
        t.start()
