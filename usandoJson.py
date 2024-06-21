# import json
import os

# with open ("personas.json", "r") as file:
#     data = json.load(file)

# for person in data:
#     name = person["nombre"]
#     age = person["edad"]
#     print(f"name:{name}, age:{age}")

os.system('echo "hola" >> hola.txt')
res = os.system('base64 hola.txt')

print(res)