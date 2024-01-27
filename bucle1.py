'''Bucle: loop, repetir una accion N veces, iteraciones.
contadores (cuenta o incrememnta)
Acumuladores (Acumulacion de valores. pej. sumar valores)
contar valores es diferent de sumar valores

contador => c = c + k
cuantos datos hay  cont = cont + 1 // cont ++ // conte+=1
acumulador => a = a + v => V es una variable (num,salario,edad,temperatura,etc)
incremento aleatorio y variable 
acumular valores  acum = acum + num  //acum+=num

'''
def list_numbers():
    # bucle que imprime lista  de numeros por pantalla 
    i=1
    status = True
    while i<=10:
        print(i)
        i+=200
    print("i:",i)
#list_numbers()

def list_numbers2():
    # bucle que imprime lista  de numeros por pantalla 
    i=1
    status = True
    while status:
        if i == 11:
            break
        print(i)
        i+=1
    print("i:",i)
#list_numbers()
#list_numbers2()

def list_numbers3():
    # bucle que imprime lista  de numeros por pantalla 
    i=1
    status = True
    while status:
        print(i)
        i+=1
        if i> 10:
            status=False
        
    print("i:",i)
#list_numbers3()

def list_numbers4():
    # bucle que imprime lista  de numeros por pantalla 
    i=1
    status = False
    while not status:
        print(i)
        i+=1
        if i> 10:
            status=True
        
    print("i:",i)
list_numbers4()