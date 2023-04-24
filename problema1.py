'''Programa que permita lanzar procesos que ingresen y retiren dinero a la vez y comprobar así si el resultado final es el esperado, de un banco'''

#Se parte de una cuenta con 100 euros y se pueden tener procesos que ingresen 100, 50 y 20 euros. Se pueden tener procesos que retiren 100, 50 y 20 euros.
#Se desea tener los siguientes procesos: 40 procesos que ingresan 100, 20 procesos que ingresan 50, 60 procesos que ingresen 20
#40 procesos que retiren 100, 20 procesos que retiren 50, 60 procesos que retiren 20

import multiprocessing

cuenta = 0

#funcion que ingrese 100 euros
def ingreso100():
    global cuenta
    cuenta += 100
