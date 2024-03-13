'''
C====> Create (INSERT INTO)
R====> Read   (SELECT)
U====> Update (UPDATEcl)
D====> Delete (DELATE)

'''

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

def list_users(op):
    #Read all the data from table users
    os.system('clear')
    cur.execute("SELECT * FROM user")
    print(cur.fetchall())

    os.system('pause')
    menu()

def search_user(op):
    os.system('clear')
    print("::: SEARCH USER BY IDENTIFICATION NUMBER :::")
    ident_num = input("Identification number: ")

    cur.execute(f"SELECT email FROM user WHERE ident_number = '{ident_num}' ")
    print(cur.fetchall())

    os.system('pause')
    menu()
def update_user(op):
    print(": UPDATE USER FORM :: :")
    iden = input("User identification: ")

    cur.execute("SELECT firtsname FROM user WHERE ident_number=?", [iden])
    print(f"Current name: {cur.fetchall()}")

    user_name = input("New user name: ")
    conf = input("Do you want to update the name? (Y/n): ")
    if conf == 'Y' or conf == 'y':
         cur.execute(f"UPDATE user SET firtsname = '{user_name}' WHERE ident_number = {iden}")
         con.commit()
    print("::: User-name has been updated successfully :: ")
    
    cur.execute(f"UPDATE user SET firtsname = '{user_name}' WHERE ident_number = {iden}")
    print("::: User-name has been updated successfully :: :")

    cur.execute("SELECT firtsname FROM user WHERE ident_number=?", [iden])
    print(f"Current name: {cur.fetchall()}")

    os.system('pause')
    menu()
def delete_user(op):
    os.system('clear')
    print("::: DELETE USER FORM :::")
    iden = input("Enter the user identification: ")

    cur.execute("SELECT firtsname, lastname FROM user WHERE ident_number=?", [iden])
    print(f"User to delete is: {cur.fetchall()}")

    conf = input("Do you want to delete the user? (Y/n): ")
    if conf == 'Y' or conf == 'y':
        cur.execute(f"DELETE FROM user WHERE ident_number = '{iden}' ")
        con.commit()
        print("::: User has been deleted successfully :::")

    cur.execute("SELECT firtsname, lastname FROM user WHERE  ident_number=?", [iden])
    print(f"Current name: {cur.fetchall()}")

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
        print("[2]. List users")
        print("[3]. Search user")
        print("[4]. Update user")
        print("[5]. Delete user")
        print("[6]. Exit")
        
        while status_opt:
            opt = input("Press an option: ")
            if opt < '1' or opt > '6':
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