'''crear una calculadora que reciba dos valores  generador aleatoriamente por consola 
y realice las operaciones aritmeticas basicas'''
from random  import randint, uniform
import os

#randint genera numeros aleatorios enteros 
#uniform genera numeros con decimales 

os.system('clear')

n1= randint(-100,100)
n2= uniform(1,45)

print(n1)
print(n2)
