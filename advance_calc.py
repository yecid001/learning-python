'''crear una calculadora que reciba dos valores por consola 
y realice las operaciones aritmeticas basicas'''

import os
os.system('clear')
def todasop(x,y,z):
    print("la suma es :", x+y )
    print("la resta es :", x-y )
    print("la multiplicacion es :", x*y )
    print("la divicion es :", x/y )

def caculator(x,y,z):

    if z == '1' :
        return x+y
    elif z=='2':
        return x-y
    elif z=='3':
        return x*y
    elif z == '4':
        if y ==0:
            return'no es posible dividir entre cero'
        else:
            return x/y
    elif z == '5':
        return todasop
    
    else :
        print(":::::fail, invalid option :::::::::")
        return 
    


#imputs
print("ingrese primer valor: ")
n1= float (input())
n2= float (input("ingrese el segundo valor: \n"))


print(":::::::Menu Calculadora::::::")

print("[1]. Suamar")
print("[2]. Restar" )
print("[3]. multiplicar")
print("[4]. dividir")
print("[5]. resultado con todas las operaciones")

opc= input("digite una opcion del menu : ")

#ans= caculator(n1,n2,opc)
ans = todasop(n1,n2,opc)
#print ("resultado : ",ans)
