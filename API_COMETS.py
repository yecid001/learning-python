'''Script description: get all data about comets.'''

import requests
import os 

os.system('clear')

def get_comets():
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    print("::::COMETS INFORMATION:::")

    try:
       response= requests.get(url)
       response.raise_for_status()


       data=response.json()
       count=0
       print ("solar menu")
       print("[1]. Planets")
       print("[2]. Moons")
       print("[3]. Star")
       print("[4]. Asteroid")
       print("[5]. Comets")
       opt = int(input("choose an option: "))

       if opt ==1:
           body_type= "Planet"
       elif opt == 2:
           body_type="Moon"
       elif opt == 3:
            body_type="Star"
       elif opt == 4:
            body_type= "Asteroid"
       elif opt==5:
            body_type= "coments"

       #total = int (input("cantidad de datos por mostrar"))
       planet = input ("escriba el planeta a buscar: ")
       for comet in data["bodies"]:

            #if comet["isPlanet"]== True:
            if comet["bodyType"] == body_type:
                print('English name', comet["englishName"])
                print('moons', comet["moons"])
                print('gravity', comet["gravity"])
                print('Is planet?', comet["isPlanet"])
                print("\n")

        #        count=count+1
         #   if count == total:
        #        break
       #print(count)
    except requests.exceptions.RequestException as e:
        print(f"api error: {e}")
get_comets()
