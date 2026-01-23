from models.connection_options.connection import DBConnectionHandler
from models.repository.minhaCollection_repository import MinhaCollectionRepository

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

minha_collection_repository = MinhaCollectionRepository(db_connection)

response = minha_collection_repository.select_many({ "name": "Dozo", "pedidos.pizza": 1 })

# print(response)
print()

response2 = minha_collection_repository.select_one({ "name": "Dozo" })

# print(response2)

# minha_collection_repository.select_if_property_exists()

# minha_collection_repository.select_many_order()

# minha_collection_repository.select_or()

# minha_collection_repository.select_by_object_id()

# minha_collection_repository.edit_registry(19)

# filtro = { "profissao": "Programador" }
# propriedades = { 
#     "endereco": {
#         "cep": "1234556",
#         "rua": "das pitangas",
#         "bairro": "chacaro",
#         "numero": 123   
#     }
# }
# minha_collection_repository.edit_many_registrys(filtro, propriedades)

# minha_collection_repository.edit_many_increment(2)

# minha_collection_repository.delete_registry()

minha_collection_repository.delete_one_registry()