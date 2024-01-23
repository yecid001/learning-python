'''sscript que genere el lanzamiento de dos dados (1-6) y
 que diga por pantalla el mensaje ganador cuando genere un par de seis 
de lo contrario, el mensaje dira, sigue intentando '''
#importo biblioteca para generar numeros aleatorios enteros 

from random import randint

# Lanzar y generar o lanzar los dos dados 
 
def dices():

    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2



d=dices()
d1= d[0]
d2 = d[1]



print("dados:", d)
print("dice1:",d1)
print("dice2 :",d2)

#print("dado1",dice1)
#print("dado2", dice2)
