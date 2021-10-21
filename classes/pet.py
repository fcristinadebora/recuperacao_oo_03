class Pet:
    status_indisponivel = "Indisponível"
    status_disponivel = "Disponível"
    status_adotado = "Adotado"

    porte_pequeno = "pequeno"
    porte_medio = "medio"
    porte_grande = "grande"

    def __init__(self, nome):
        self._nome = nome
        self._porte = ''
        self._status = Pet.status_disponivel

    def set_porte(self, porte):
        if (porte != Pet.porte_pequeno
            and porte != Pet.porte_medio
            and porte != Pet.porte_grande
        ):
            print("Porte inválido")
            return

        self._porte = porte

    def mostrar_detalhes(self):
        print("Nome: " + self._nome)
        print("Porte: " + self._porte)
        print("Status de adoção: " + self._status)

    def set_status(self, status):
        if (status != Pet.status_indisponivel
            and status != Pet.status_disponivel
            and status != Pet.status_adotado
        ):
            print("Status inválido")
            return

        self._status = status

    def get_nome(self):
        return self._nome