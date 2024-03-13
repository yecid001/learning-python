from database import con, cur
import os
import bcrypt

status_menu = True
global status_op

def hash_password(passwd):
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())

def create_user(op):
    #Create a new user
    os.system('clear')

    print("::: Signup form :::")
    fname = input("Your firstname: ")
    lname = input("Your lastname: ")
    ident = input("Your ident number: ")
    email = input("Your email: ")
    passwd = input("Your password: ")
    passwd_hashed = hash_password(passwd)

    new_user = f'''
        INSERT INTO 
            user (firstname, latsname, ident_number, email, password) 
            VALUES('{fname}', '{lname}', '{ident}', '{email}', "{passwd_hashed}")
    '''
    con.execute(new_user)
    con.commit()

    print("::: New user has been created sucessfully :::")
    os.system('pause')
    menu()

def menu():
    global opt
    status_opt = True
    while status_menu: 
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: MAIN MENU ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. Create a new user")
        print("[2]. Create student")
        print("[3]. Create identification type")
        print("[4]. Create person")
        print("[5]. Create cityr")
        print("[6]. Create department")
        print("[7]. Create country")
        
        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '7':
                print(".:::::: Invalid option, try again.")
            else :
                status_opt = False

        if opt == '1':
            create_user(opt)
        elif opt == '2':
            list_users(opt)
        elif opt == '3':
            search_user(opt)
        elif opt == '4':
            update_user(opt)
        elif opt == '5':
            delete_user(opt)
        else:
            print("::: See 'u soon :::")
            exit()
        
menu()

#Close connection
con.close()