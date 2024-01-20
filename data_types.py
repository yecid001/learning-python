# Tipos de datos en Python
# Python es un lenguaje dinamicamente tipado, no requiere identificar variables ()
# Python es un lenguaje interpretado

#1. Numéricos
##numero Z => int
num1= 42
print ("num1:", type(num1))
##numero Flotantes o decimales (reales)=> float
num2 =50.5
print ("num2", type(num2))
##numero complex o numeros complejos => complex
num3 = 2j
print ("num3", type(num3))


#2. Cadena

my_name = "cesar"
my_lastname ='Riascos'
Profile=''' cesar es una buena persona :c  
 y le gustan los gatos'''
address = "la union calle 2 n 234"
phone_number= "3225264831"
print("profile",type(Profile))
print("address",type(address))
print("phone_number",type(phone_number))

#suma aritmetica
a=1
b=1
suma1=a+b


#suma de cadena (concatenacion)
c="1"
d="1"
suma2=c+d



print("sum1",suma1)#2
print("sum2",suma2)#11

#3. Lógicos (valores boleanos)

usuario_activo=True
print("usuario activo",type(usuario_activo))

pago_realizado=False
print("pago realizado",type(pago_realizado))


#4. Listas
frutas=['apple', 'banana']
print("frutas",type(frutas))

colors=['blue','red']
print("colors",colors,type(colors))

detodito=['cesar',20,400000,'la union',1.68]
print(detodito)

#5. Tuplas
#6. Diccionarios
#7. Conjuntos