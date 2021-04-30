# create_database
import sqlite3

#conectando...
conn = sqlite3.connect('conflitos.db')
#definindo o cursor
cursor = conn.cursor()


#criando a tabela (schema)
cursor.execute("""
CREATE TABLE CONFLITOS(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    role1 TEXT NOT NULL,
    role2 TEXT NOT NULL,
    conflito INTEGER NOT NULL
);
""")

print("Tabela criada com sucesso.")
#desconectando
conn.close()