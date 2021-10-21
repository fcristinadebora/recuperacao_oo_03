from .ong import Ong
class Menu:

    def __init__(self):
        self.executando = True
        self._ongs = []

    def listar_opcoes(self):
        print("Bem vindo ao Gestor de ONGs da Debora!")
        print("Operações possíveis:")
        print("1 - Cadastrar ONGs")
        print("2 - Listar ONGs")
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