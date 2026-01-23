from bson.objectid import ObjectId #Json binario
from typing import Dict, List

class MinhaCollectionRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "minhaCollection"
        self.__db_connection = db_connection


    #Metodos
    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
    
    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents
    
    def select_many(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            filter, #Filtro
            {"endereco": 0, "_id": 0} #Opções de Retorno
            )
        
        response = []
        for elementos in data: 
            response.append(elementos)

        return response
    
    def select_one(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filter, { "_id": 0 })
        return response
    
    def select_if_property_exists(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "cpf": { "$exists": True }})
        for elementos in data:
            print(elementos)

    def select_many_order(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            { "name": "Dozo" }, #Filtro
            {"endereco": 0, "_id": 0} #Opções de Retorno
        ).sort([("pedidos.pizza", -1 )])#ou 1 para crescente #Ordenar do maior pro menor
        
        for elementos in data: 
            print(elementos)

    def select_or(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "$or": [{ "name": "Dozo" }, { "Legal": { "$exists": True } }] })
        for elementos in data:
            print(elementos)
            print()

    def select_by_object_id(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "_id": ObjectId("69727c0cbeadd9537c8dfc6a") })
        for elemento in data:
            print(elemento)

    def edit_registry(self, idade) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one(
            { "_id": ObjectId("6973cd5189065bacae045c5e") },  #Filtro
            { "$set": { "idade": idade } } # Campo de edição
        )   
        print(data.modified_count)

    def edit_many_registrys(self, filtro, propriedades) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(
            filtro,  #Filtro
            { "$set": propriedades }
        )   
        print(data.modified_count)

    def edit_many_increment(self, num) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(
            { "_id": ObjectId("6973cd5189065bacae045c5e") },  #Filtro
            { "$inc": { "idade": num } } #Incrementador $inc
        )   
        print(data.modified_count)

    def delete_many_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many( { "profissao": "Programador" })
        print(data.deleted_count)

    def delete_one_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one( { "_id": ObjectId("6973cd6e89065bacae045c60") } ) 
        print(data.deleted_count)