'''
#application programming interface
#NASA API : https://api.nasa.gov/
#get coments
# API_KEY_NASA:  DGM1lH9YkXDm1pieCUGJBrKs6NNqdcDVoKp1LGqg
#desarrolladores: yecid riascos
#date: 24012024

https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key=DGM1lH9YkXDm1pieCUGJBrKs6NNqdcDVoKp1LGqg

datos de cometas'''

import requests
import os

os.system('clear')
def get_comet_data(api_key):
    print("::::::::::comete information:::::::::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"


    try: 
        response = requests.get(url)
        response.raise_for_status() # valida si se presenta algun error en la peticion
        #realizar la solicitud a la API
        #convertit la rspuestas a formato json (js object notation)
        datos=response.json()

        print(f"comet name{datos['name']}")
        print(f"Absolute magnitude:{datos['absolute_magnitude_h']}")
        print(f"Estimated Diameters km :{datos['estimated_diameter']['kilometers']['estimated_diameter_max']}")
        print(f"Estimated diameter max (FT): {datos['estimated_diameter']['feet']['estimated_diameter_max']}")

    except requests.exceptions.RequestException as e:
        print(f"error al realizar la peticion a la API de NASA: {e}")

api_key_nasa = 'DGM1lH9YkXDm1pieCUGJBrKs6NNqdcDVoKp1LGqg'

get_comet_data(api_key_nasa)
    

