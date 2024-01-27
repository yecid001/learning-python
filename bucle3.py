'''bucle que genere un n cantidad de numeros entero (+-) aleatorios
el usuario debe digitat la cantidad de numeros a generar
al finalizar, debe presentar por pantalla el sig reporte:
- total de numeros 
- cuantos nros son pares
- cuantos nros son impares
- cuantos nros son positivos
- cuantos nros son negativos 
- suma de pares
- resta de impares

'''

import os
import random
from random import randint

os.system('clear')


def numbers_generator(cant):
    i=1
    pares=0
    impares=0
    positivos=0
    negativos=0
    sum_pos=0
    sum_neg=0
    while i<=cant:
        num=random.randint(-10,10)
        
        print(num)
        if num % 2 ==0 :
            pares= pares +1
        else :
            impares +=1
        if num>0:
            positivos=positivos+1
        else :
            negativos=negativos+1

        i+=1
    print(f"numeros ingresados: {cant}")
    print(f"pares generados : {pares}")
    print(f"impares generados : {impares}")
    print(f"total positivos : {positivos}")
    print(f"total negativo : {negativos}")

cant_num = int(input("que cantidad de numeros quieres generar :"))
numbers_generator(cant_num)
