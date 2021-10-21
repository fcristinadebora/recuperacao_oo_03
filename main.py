from classes.menu import Menu

menu = Menu()

while menu.executando == True:
    menu.listar_opcoes()
    menu.executar_operacao()