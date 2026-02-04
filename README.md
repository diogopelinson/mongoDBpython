# MongoDB + Python (PyMongo) Playground

Um projeto simples e direto para praticar conexao, consultas e operacoes CRUD no MongoDB usando Python e o driver `pymongo`.

## O que tem aqui

- Conexao com MongoDB via `MongoClient`
- Repositorio com metodos de consulta e atualizacao
- Exemplos de `find`, `update`, `delete`, `sort`, `ObjectId` e indice TTL

## Estrutura do projeto

- `run.py` script principal com exemplos de uso
- `models/connection_options/connection.py` handler de conexao com MongoDB
- `models/connection_options/mongo_db_configs.py` configuracoes de conexao
- `models/repository/minhaCollection_repository.py` repositorio de consultas e updates
- `docker/docker-compose.yml` container MongoDB para uso local

## Requisitos

- Python 3
- MongoDB local ou container via Docker
- Dependencia Python: `pymongo`

## Setup rapido

1. Instale a dependencia:

```bash
pip install pymongo
```

2. Ajuste as credenciais e o banco em:

`models/connection_options/mongo_db_configs.py`

## Subindo MongoDB com Docker

O `docker-compose.yml` cria um MongoDB com usuario `admin` e senha `admin123`.

```bash
docker compose -f docker/docker-compose.yml up -d
```

Atencao: o compose cria o banco inicial como `appdb`, mas o codigo esta configurado com `DB_NAME = "meuBanco"`.
Se quiser usar o banco do compose, atualize o `DB_NAME` para `appdb` em `models/connection_options/mongo_db_configs.py`.

## Rodando o projeto

```bash
python run.py
```

O `run.py` esta preparado para testar diferentes operacoes. Voce pode comentar ou descomentar os metodos no arquivo
para executar cada exemplo.

## Exemplo rapido de insercao

```python
from datetime import datetime

documento = {
    "nome": "Arnaldo",
    "idade": 35,
    "data_de_criacao": datetime.now(),
}

minha_collection_repository.insert_document(documento)
```

## Exemplos disponiveis no repositorio

- `select_many` com filtro e projecao
- `select_one`
- `select_if_property_exists`
- `select_many_order` com sort
- `select_or`
- `select_by_object_id`
- `edit_registry`
- `edit_many_registrys`
- `edit_many_increment`
- `delete_many_registry`
- `delete_one_registry`
- `create_index_ttl`

## Observacoes

- Para usar `ObjectId`, verifique se o ID existe na sua colecao.
- O metodo `create_index_ttl` cria um indice de expiracao por tempo para o campo `data_de_criacao`.

---

## Estrutura de pastas

```
├── 📁 docker
│   └── ⚙️ docker-compose.yml
├── 📁 models
│   ├── 📁 connection_options
│   │   ├── 🐍 connection.py
│   │   └── 🐍 mongo_db_configs.py
│   └── 📁 repository
│       └── 🐍 minhaCollection_repository.py
├── ⚙️ .gitignore
├── 📝 README.md
└── 🐍 run.py
```
