from cassandra.cluster import Cluster

# Conectar ao Cassandra (presumindo que o Cassandra está rodando localmente ou remotamente)
cluster = Cluster(['127.0.0.1'])  # Endereço IP do nó Cassandra
session = cluster.connect()

# Criar um Keyspace e uma Tabela
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS example WITH REPLICATION = {
        'class': 'SimpleStrategy',
        'replication_factor': 3
    }
""")
session.set_keyspace('example')

# Criar uma tabela
session.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id UUID PRIMARY KEY,
        username TEXT,
        email TEXT
    )
""")

# Inserir dados na tabela
from uuid import uuid4
session.execute("""
    INSERT INTO users (user_id, username, email) VALUES (%s, %s, %s)
""", (uuid4(), 'john_doe', 'john.doe@example.com'))

# Ler dados
rows = session.execute('SELECT * FROM users')
for row in rows:
    print(row)

# Fechar a sessão
cluster.shutdown()