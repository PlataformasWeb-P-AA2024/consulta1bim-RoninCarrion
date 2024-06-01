from pymongo import MongoClient

client = MongoClient()
db = client["tennisDb"]
collection = db["tournaments"]

print("<--- Programa que imprime información de los torneos --->")
data = collection.find()

for torneo in data:
    print("""
+-------------------------------------------+
| Se ha encontrado la siguiente información |
+-------------------------------------------+
          """)
    for key, data in torneo.items():
        if(key == '_id'):
            continue
        print(f"""\t> {key}: {data}""")

