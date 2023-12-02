"""
Dao - Data access object
Implementa a conexao com o
banco de dados.
"""
from database import Database
from entidades import Cliente, Produto


class FavoritoDao:
    
    def save (self, cliente, produto):
        conn = Database.get_connection()
        
        resposta = conn.execute(
        f"""
        
        SELECT produto_id FROM favoritos WHERE produto_id = {produto.id}
        """
        )
        
        resultado = resposta.fetchone()
        if resultado == None:
            conn.execute(
                f"""
                INSERT INTO favoritos (
                    cliente_id, produto_id            
                ) VALUES (?, ?)
                """,
                (
                    cliente.id,  
                    produto.id, 
                )
            )
            conn.commit()
            conn.close()
        else:
            conn.close()
        
    def favoritos (self, cliente, produto):
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO favoritos (
                cliente_id, produto_id            
            ) VALUES (?, ?)
            """,
            (
                cliente.id,  
                produto.id, 
            )
        )
        conn.commit()
        
    def deletefavoritos (self, id):
        conn = Database.get_connection()
        conn.execute(
            f"""
            DELETE FROM favoritos WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()
    
    def procurarfavoritos(self):
        conn = Database.get_connection()
        resposta = conn.execute("""
        SELECT p.id, nome, preco, marca, f.id FROM produto p INNER JOIN favoritos f on f.produto_id = p.id WHERE f.cliente_id = 1
        """
        )
        resultado = resposta.fetchall()
        
        resultado = [
            { 
                "id": produto[0], 
                "nome": produto[1],
                "preco": produto[2],
                "marca": produto[3],
                "favorito": produto[4],
            } for produto in resultado]
        conn.close()
        return resultado

class ProdutoDao:
    def save(self, produto):
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO produto (
                nome, preco, marca            
            ) VALUES (?, ?, ?)
            """,
            (
                produto.nome,  
                produto.preco, 
                produto.marca,
            )
        )
        conn.commit()
        conn.close()

    def update(self, produto):
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE produto SET nome = ?, preco = ?, marca = ?
            """,
            (
                produto.nome,
                produto.preco,
                produto.marca,
                produto.id
            )
        )
        conn.commit()
        conn.close()
        
    def delete(self, id):    
        conn = Database.get_connection()
        conn.execute(
            f"""
            DELETE FROM produto WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()

        
    # READ
    def find_all(self):
        conn = Database.get_connection()
        res = conn.execute("""
        SELECT id, nome, preco, marca FROM produto
        """
        )
        results = res.fetchall()
        results = [
            { 
                "id": produto[0], 
                "nome": produto[1],
                "preco": produto[2],
                "marca": produto[3],
            } for produto in results]

        conn.close()
        return results
    
    def get_produto(self, id):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, preco, marca  FROM produto WHERE id = {id}
        """
        )
        row = res.fetchone()
        
        produto = Produto( 
            row[1],
            row[2],
            marca = row[3],
            id = row[0]            
            
        )
        conn.close()
        return produto
    
    def busca(self, busca):
        conn = Database.get_connection()
        resposta = conn.execute(f"""
        SELECT * FROM produto
        WHERE nome LIKE "%{busca}%"
        """
        )
        resultado = resposta.fetchall()
        
        resultado = [
            { 
                "id": produto[0], 
                "nome": produto[1],
                "preco": produto[2],
                "marca": produto[3],
            } for produto in resultado]
        conn.close()
        return resultado

class ClienteDao:

    def save(self, cliente):
        """
        Realiza o INSERT na tabela cliente
        """
        # obtem uma conexao com o banco:
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO cliente (
                nome, cpf, cep, email            
            ) VALUES (?, ?, ?, ?)
            """,
            (
                cliente.nome,  
                cliente.cpf, 
                cliente.cep,
                cliente.email, 
            )
        )
        conn.commit()
        conn.close()


    def update(self, cliente):
        """
        Realiza UPDATE do cliente
        """
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE cliente SET nome = ?, cpf = ?, cep = ?, email = ?
            WHERE id = ?
            """,
            (
                cliente.nome,
                cliente.cpf,
                cliente.cep,
                cliente.email,
                cliente.id
            )
        )
        conn.commit()
        conn.close()

    def delete(self, id):
        """
        Remove um cliente de acordo com o id fornecido
        """
        conn = Database.get_connection()
        conn.execute(
            # Query
            # Hard Delete (cuidado!)
            f"""
            DELETE FROM cliente WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()


    def find_all(self):
        conn = Database.get_connection()
        res = conn.execute("""
        SELECT id, nome, cpf, cep, email, data_cadastro FROM cliente
        """
        )
        # executa o SELECT
        results = res.fetchall()
        # results eh um vetor

        # versao 1
        results = [
            { 
                "id": cliente[0], 
                "nome": cliente[1],
                "cpf": cliente[2],
                "cep": cliente[3],
                "email": cliente[4],
                "data_cadastro": cliente[5],
            } for cliente in results]

        conn.close()
        return results


    def get_cliente(self, id):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, email, cpf, cep, data_cadastro  FROM cliente WHERE id = {id}
        """
        )
        row = res.fetchone()
        
        # cria um objeto cliente para armazenar resultado do SELECT:
        cliente = Cliente( 
            row[1],
            row[2],
            id = row[0],
            cpf = row[3],
            cep = row[4],             
            data_cadastro = row[5]
        )
        conn.close()
        return cliente