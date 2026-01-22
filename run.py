from models.connection_options.connection import DBConnectionHandler

db_handle = DBConnectionHandler()
conn1 = db_handle.get_db_connection()
print(conn1)    #None

print("---------------------------------------")

db_handle.connect_to_db()
conn2 = db_handle.get_db_connection()
print(conn2)    # Alguma coisa que não é None

collection = conn2.get_collection("minhaCollection")


collection.insert_one( { 
    "Legal": "Sim",
    "Numeros_da_sorte": [123, 124, 567]
 } )