"""
Classe utilitária para 
ajudar na inicilização do 
banco de dados
"""
import sqlite3

class Database:

    @staticmethod
    def create_db():
        """ criar as tabela """
        conn = sqlite3.connect('banco.db')
        print('Criando banco de dados...')
        with open('schema.sql') as f:
            # executa o create table, insert, ...
            conn.executescript(f.read())
        conn.commit()
        conn.close()

    @staticmethod
    def get_connection():
        """ obter uma conexao com o BD """
        conn = sqlite3.connect('banco.db')
        return conn

if __name__ == '__main__':
    # descomentar linha abaixo para gerar o arquivo banco.db
    #Database.create_db()
    pass