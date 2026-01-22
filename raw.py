from pymongo import MongoClient

connection_string = "mongodb://admin:admin123@localhost:27017/?authSource=admin"
client = MongoClient(connection_string)
db_connection = client["meuBanco"]

print(db_connection)
print()
collection = db_connection.get_collection("minhaCollection")

print(collection)
print()
search_filter = { "email": "diogo@email.com" } 

response = collection.find(search_filter)


for registry in response:
    print(registry)


collection.insert_one( { 
    "Legal": "Sim",
    "Numeros_da_sorte": [123, 124, 567]
 } )