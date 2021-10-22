from .ong import Ong
from .pet import Pet

class Menu:

    def __init__(self):
        self.executando = True
        self._ongs = []

    def listar_opcoes(self):
        print("Bem vindo ao Gestor de ONGs da Debora!")
        print("Operações possíveis:")
        print("1 - Cadastrar ONGs")
        print("2 - Listar ONGs")
        print("3 - Editar ONG")
        print("4 - Excluir ONG")
        print("5 - Cadastrar Pet")
        print("6 - Mostrar detalhes de ONG")
        print("7 - Alterar status do Pet")
        print("8 - Excluir Pet")
        print("99 - Encerrar programa")

    def ler_operacao(self):
        operacao = input("Digite a operação desejada > ")
        return operacao

    def executar_operacao(self):
        operacao = self.ler_operacao()

        if (operacao == "1"):
            self.cadastrar_ong()
        if (operacao == "2"):
            self.listar_ongs()
        if (operacao == "3"):
            self.editar_ong()
        if (operacao == "4"):
            self.excluir_ong()
        if (operacao == "5"):
            self.cadastrar_pet()
        if (operacao == "6"):
            self.mostrar_detalhes_ong()
        if (operacao == "7"):
            self.alterar_status_pet()
        if (operacao == "8"):
            self.excluir_pet()
        if (operacao == "99"):
            self.encerrar_programa()

        print("")

    def encerrar_programa(self):
        print("Encerrando execução")
        self.executando = False

    def cadastrar_ong(self):
        print("")
        print(" ---- Cadastrar ONG --- ")
        nome = input("Nome da ONG: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        nome_responsavel = input("Nome do responsável: ")

        ong = Ong(nome, endereco, telefone, nome_responsavel)
        self._ongs.append(ong)

    def listar_ongs(self):
        print("")
        print(" ---- Listar ONG --- ")
        for indice, ong in enumerate(self._ongs):
            print(str(indice) + " - " + ong.get_nome())

    def editar_ong(self):
        print("")
        print(" ---- Editar ONG --- ")

        ong_editando = self.selecionar_ong()
        if (ong_editando == None):
            return

        nome = input("Nome da ONG: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        nome_responsavel = input("Nome do responsável: ")

        ong_editando.set_nome(nome)
        ong_editando.set_endereco(endereco)
        ong_editando.set_telefone(telefone)
        ong_editando.set_nome_responsavel(nome_responsavel)

    def excluir_ong(self):
        print("")
        print(" ---- Excluir ONG --- ")

        ong_excluir = self.selecionar_ong()
        if (ong_excluir == None):
            return

        self._ongs.remove(ong_excluir)

    def selecionar_ong(self):
        self.listar_ongs()
        indice_ong = input("Digite o numero da ONG > ")

        try:
            ong = self._ongs[int(indice_ong)]
        except:
            print("Ong inválida")
            return None

        return ong

    def cadastrar_pet(self):
        print("")
        print(" ---- Cadastrar Pet --- ")

        ong = self.selecionar_ong()
        if (ong == None):
            return

        nome = input("Nome do pet: ")
        porte = input("Porte: [" + Pet.porte_pequeno + "|" + Pet.porte_medio + "|" + Pet.porte_medio + "]: ")

        pet = Pet(nome)
        pet.set_porte(porte)
        ong.add_pet(pet)

    def mostrar_detalhes_ong(self):
        ong = self.selecionar_ong()
        if (ong == None):
            return

        ong.exibir_detalhes()

    def alterar_status_pet(self):
        ong = self.selecionar_ong()
        if (ong == None):
            return

        pet = self.selecionar_pet(ong)
        if (pet == None):
            return

        novo_status = input("Digite o status do pet [" + Pet.status_indisponivel + "|" + Pet.status_disponivel + "|" + Pet.status_adotado + "]: ")
        pet.set_status(novo_status)

    def excluir_pet(self):
        ong = self.selecionar_ong()
        if (ong == None):
            return

        pet = self.selecionar_pet(ong)
        if (pet == None):
            return

        ong.remove_pet(pet)

    def selecionar_pet(self, ong):
        for indice, pet in enumerate(ong.get_pets()):
            print(str(indice) + " - " + pet.get_nome())

        indice_pet = input("Digite o numero do Pet > ")
        try:
            pets = ong.get_pets()
            pet = pets[int(indice_pet)]
        except:
            print("Pet Inválido")
            return None

        return pet