class Produto:
    def __init__(self, nome, preco, marca=None, id=None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.marca = marca
        self.added = marca

class Cliente:
    def __init__(self, nome, email, id=None, cpf=None, cep=None, data_cadastro=None):
        """ Metodo construtor para cliente """
        # atributos obrigatorios:
        self.nome = nome
        self.email = email
        # atributos opcionais:
        self.id = id
        self.cpf = cpf
        self.cep = cep
        self.data_cadastro = data_cadastro