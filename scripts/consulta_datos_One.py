from pymongo import MongoClient

client = MongoClient()
db = client["tennisDb"]
collection = db["tournaments"]

print("<--- Programa que imprime información de los torneos --->")
data = collection.find_one({'Tournament': 'Brisbane International'})


print("""
    +-------------------------------------------+
    | Se ha encontrado la siguiente información |
    +-------------------------------------------+
          """)

# print(data)
for key, data in data.items():
    if(key == '_id'):
            continue
    print(f"""\t> {key}: {data}""")

