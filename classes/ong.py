class Ong:
    def __init__(self, nome, endereco, telefone, nome_responsavel):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._nome_responsavel = nome_responsavel

    def get_nome(self):
        return self._nome