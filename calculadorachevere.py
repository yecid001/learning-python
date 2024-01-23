def todasop(x, y):
    print("La suma es:", x + y)
    print("La resta es:", x - y)
    print("La multiplicación es:", x * y)
    if y != 0:
        print("La división es:", x / y)
    else:
        print("No es posible dividir entre cero")

def calculator(x, y, z):
    if z == '1':
        return x+y
    elif z == '2':
        return x - y
    elif z == '3':
        return x * y
    elif z == '4':
        if y != 0:
            return x / y
        else:
            return 'No es posible dividir entre cero'
    elif z == '5':
        todasop(x, y)
        
    else:
        print("::::: Error, opción no válida ::::::::::::")
        return 'vulva a iniciar la calculadora y seleccione una opcion '

# Inputs
print("Ingrese el primer valor:")
n1 = float(input())
n2 = float(input("Ingrese el segundo valor:\n"))

print("::::::: Menu Calculadora :::::::")

print("[1]. Sumar")
print("[2]. Restar")
print("[3]. Multiplicar")
print("[4]. Dividir")
print("[5]. Resultado con todas las operaciones")

opc = input("Digite una opción del menú: ")



ans = calculator(n1, n2, opc)


#if ans != None:
print("Resultado:", ans)

