import os
import psycopg

def conectar():
    conexao = psycopg.connect(dbname = "rpg",
                user = "postgres",
                password = os.getenv("DB_PASSWORD"),
                host = "localhost",
                port = 5432)

    return conexao