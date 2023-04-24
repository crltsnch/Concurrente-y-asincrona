'''Programa que permita lanzar procesos que ingresen y retiren dinero a la vez y comprobar así si el resultado final es el esperado, de un banco'''

#Se parte de una cuenta con 100 euros y se pueden tener procesos que ingresen 100, 50 y 20 euros. Se pueden tener procesos que retiren 100, 50 y 20 euros.
#Se desea tener los siguientes procesos: 40 procesos que ingresan 100, 20 procesos que ingresan 50, 60 procesos que ingresen 20
#40 procesos que retiren 100, 20 procesos que retiren 50, 60 procesos que retiren 20
#comprobar tras la ejecución que la cuenta tiene 100 euros, como al principio


import multiprocessing

cuenta = 100

#funcion que ingrese 100, 50 o 20 euros
def ingreso():
    cantidad = input('Cuanto dinero desea ingresar?')
    global cuenta
    if cantidad != 100:
        if cantidad != 50:
            if cantidad != 20:
                print('No se puede ingresar esa cantidad')
    else:
        cuenta += ingreso
        print('Se ha ingresado', cantidad, 'euros')
        print('La cuenta tiene', cuenta, 'euros')

#funcion que retire 100, 50 o 20 euros
def retiro():
    cantidad = input('Cuanto dinero desea retirar?')
    global cuenta
    if cantidad != 100:
        if cantidad != 50:
            if cantidad != 20:
                print('No se puede retirar esa cantidad')
    else:
        if cantidad > cuenta:
            print('No se puede retirar esa cantidad')
        else:
            cuenta -= retiro
            print('Se ha retirado', cantidad, 'euros')
            print('La cuenta tiene', cuenta, 'euros')

for i in range(40):
    p = multiprocessing.Process(target=ingreso)
    p.start()

#hacer 20 procesos que ingresen 50 euros
for i in range(20):
    p = multiprocessing.Process(target=ingreso)
    p.start()
    p.join()

#hacer 60 procesos que ingresen 20 euros
for i in range(60):
    p = multiprocessing.Process(target=ingreso)
    p.start()
    p.join()

#hacer 40 procesos que retiren 100 euros
for i in range(40):
    p = multiprocessing.Process(target=retiro)
    p.start()
    p.join()

for i in range(20):
    p = multiprocessing.Process(target=retiro)
    p.start()
    p.join()

for i in range(60):
    p = multiprocessing.Process(target=retiro)
    p.start()
    p.join()

print('La cuenta tiene', cuenta, 'euros')

#comprobar que la cuenta tiene 100 euros
if cuenta == 100:
    print('La cuenta tiene 100 euros')

