import requests
import yaml


url= "http://10.8.183.87:2224"

pokedata= requests.get(url).json()

print(yaml.dump(pokedata))
