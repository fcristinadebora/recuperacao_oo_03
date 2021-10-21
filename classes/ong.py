class Ong:
    def __init__(self, nome, endereco, telefone, nome_responsavel):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._nome_responsavel = nome_responsavel

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def set_endereco(self, endereco):
        self._endereco = endereco

    def set_telefone(self, telefone):
        self._telefone = telefone

    def set_nome_responsavel(self, nome_responsavel):
        self.nome_responsavel = nome_responsavel