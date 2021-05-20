import json
#from utils.file_operations import save_to_file

import PythonWithFiles.utils.file_operations
PythonWithFiles.utils.file_operations.save_to_file("1asdasd","dumpfilke.txt")

with open("Sample.json", 'r') as file:
    contents = json.load(file)

print(contents['friends'][0])

cars = [
    {"make": "ford", "model": "focus"},
    {"make": "honda", "model": "Civic"},
]

with open("dumpfile.txt","w") as file:
    json.dump(cars,file)

#string to json

cars = """[
    {"make": "ford", "model": "focus"},
    {"make": "honda", "model": "Civic"}
]"""
carJson = json.loads(cars)
print(carJson[1]["model"])