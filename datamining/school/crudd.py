from school_db import con, cur, sqlite3
from datetime import datetime
import os 

status_menu = True
global status_op

def create_country(op):
  os.system('clear')

  nombre = input("Ingrese el nombre del país: ")
  abreviatura = input("Ingrese la abreviatura del país: ")
  descripcion = input("Ingrese la descripción del país: ")

  fecha_actual = datetime.now()

  nuevo_pais = f"""
    INSERT INTO
    Country (name, abrev, descrip, created_at, updated_at)
    VALUES ('{nombre}', '{abreviatura}', '{descripcion}', '{fecha_actual}', '{fecha_actual}')
  """

  cur.execute(nuevo_pais)
  con.commit()
  print("Registro de país creado con éxito.")
  os.system('pause')
  menu()

def create_department(op):
  os.system('clear')
  nombre = input("Ingrese el nombre del departamento: ")
  abreviatura = input("Ingrese la abreviatura del departamento: ")
  descripcion = input("Ingrese la descripción del departamento: ")
  cur.execute("SELECT * FROM Country")
  paises = cur.fetchall()
  print("Países disponibles:")
  for pais in paises:
    print(f"ID: {pais[0]} - Nombre: {pais[1]}")
  id_pais = input("Ingrese el ID del país al que pertenece el departamento: ")

  fecha_actual = datetime.now()

  nuevo_departamento = f"""
  INSERT INTO Department (name, abrev, descrip, id_country, created_at, updated_at)
  VALUES ('{nombre}', '{abreviatura}', '{descripcion}', '{id_pais}', '{fecha_actual}', '{fecha_actual}')
  """
  cur.execute(nuevo_departamento)
  con.commit()
  print("Registro de departamento creado con éxito.")
  os.system('pause')
  menu()

def create_city(op):
    os.system('clear')

    nombre = input("Ingrese el nombre de la ciudad: ")
    abreviatura = input("Ingrese la abreviatura de la ciudad: ")
    descripcion = input("Ingrese la descripción de la ciudad: ")
    cur.execute("SELECT * FROM Department")
    departamentos = cur.fetchall()
    # Mostramos la lista de departamentos al usuario
    print("Departamentos disponibles:")
    for departamento in departamentos:
        print(f"ID: {departamento[0]} - Nombre: {departamento[1]}")

    id_departamento = input("Ingrese el ID del departamento al que pertenece la ciudad: ")

    fecha_actual = datetime.now()

    nueva_ciudad = f"""
        INSERT INTO
            City (name, abrev, descrip, id_depart, created_at, updated_at)
            VALUES ('{nombre}', '{abreviatura}', '{descripcion}', '{id_departamento}', '{fecha_actual}', '{fecha_actual}')
    """

    cur.execute(nueva_ciudad)
    con.commit()
    print("Registro de ciudad creado con éxito.")
    os.system('pause')
    menu()

def create_identification_type(op):
    os.system('clear')
    id_identificacion = input("Ingrese el ID del tipo de identificación: ")
    nombre = input("Ingrese el nombre del tipo de identificación: ")
    abreviatura = input("Ingrese la abreviatura del tipo de identificación: ")
    descripcion = input("Ingrese la descripción del tipo de identificación: ")


    fecha_actual = datetime.now()

    nuevo_tipo_identificacion = f"""
    INSERT INTO 
        Identification_types (id_ident_type, name, abrev, descrip, created_at, updated_at)
        VALUES ('{id_identificacion}', '{nombre}', '{abreviatura}', '{descripcion}', '{fecha_actual}', '{fecha_actual}')
    """

    cur.execute(nuevo_tipo_identificacion)
    con.commit()
    print("Registro de tipo de identificación creado con éxito.")
    os.system('pause')
    menu()

def create_person(op):
    os.system('clear')
    # Importamos la librería datetime para obtener la fecha actual


    # Pedimos al usuario que ingrese los datos
    id_persons = input("Ingrese su ID personal: ")
    first_name = input("Ingrese el primer nombre de la persona: ")
    last_name = input("Ingrese el apellido de la persona: ")
    id_ident_type = input("Ingrese el ID del tipo de identificación de la persona: ")
    ident_number = input("Ingrese el número de identificación de la persona: ")
    id_exp_city = input("Ingrese el ID de la ciudad de expedición de la identificación: ")
    address = input("Ingrese la dirección de la persona: ")
    mobile = input("Ingrese el número de teléfono móvil de la persona: ")
    id_users = input("Ingrese el ID del usuario asociado a la persona: ")

    # Obtenemos la fecha actual
    fecha_actual = datetime.now()

    # Creamos la consulta usando f-string with placeholders for data and formatted date
    nueva_persona = f'''
        INSERT INTO
             Persons (id_persons, first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_users, created_at, updated_at)
             VALUES ('{id_persons}', '{first_name}', '{last_name}', '{id_ident_type}', '{ident_number}', '{id_exp_city}', '{address}', '{mobile}', '{id_users}', '{fecha_actual}', '{fecha_actual}')
    '''
    
    # Ejecutamos la consulta
    cur.execute(nueva_persona)
    con.commit()
    # Confirmamos la inserción de los datos
    print("¡Los datos se han insertado correctamente!")

    os.system('pause')
    menu()

def create_student(op):
    os.system('clear')
    id_stu = input ("Ingres el id del nuevo estudiante : ")
    codigo = input("Ingrese el código del estudiante: ")
    id_persona = input("Ingrese el ID de la persona: ")

    fecha_actual = datetime.now()
    nuevo_estudiante = f"""
        INSERT INTO Students (id_Student, code, id_persons, status, created_at, updated_at)
        VALUES ('{id_stu}', '{codigo}', '{id_persona}', 0, '{fecha_actual}', '{fecha_actual}')
        """

    cur.execute(nuevo_estudiante)

    con.commit()
    print("Registro de estudiante creado con éxito.")
    os.system('pause')
    menu()

def create_user(op):
    os.system('clear')

    id_user = input ("Ingres el id del nuevo usuario : ")
    email = input("Ingrese el correo electrónico del usuario: ")
    password = input("Ingrese la contraseña del usuario: ")

   
    fecha_actual = datetime.now()

    nuevo_usuario = f"""
        INSERT INTO
        Users (id_users, email, password, status, created_at, updated_at)
        VALUES ('{id_user}','{email}', '{password}', 0, '{fecha_actual}', '{fecha_actual}')
    """

    cur.execute(nuevo_usuario)

    con.commit()
    print("Registro de usuario creado con éxito.")

    os.system('pause')
    menu()

def menu():
    status_opt = True
    while status_menu:
        os.system("clear")
        print("===== Main Menu =====")
        print("[1] Create country")
        print("[2] Create department")
        print("[3] Create city")
        print("[4] Create identification type")
        print("[5] Create person")
        print("[6] Create student")
        print("[7] Create user")
        print("[8] Exit")

        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '8':
                print(".:::::: Invalid option, try again.")
            else :
                status_opt = False

        if opt == '1':
            create_country(opt)
        elif opt == '2':
            create_department(opt)
        elif opt == '3':
            create_city(opt)
        elif opt == '4':
            create_identification_type(opt)
        elif opt == '5':
            create_person(opt)
        elif opt == '6':
            create_student(opt)
        elif opt == '7':
            create_user(opt)
        else:
            print("::: See 'u soon :::")
            exit()
            
menu()

#close connection
con.close()
