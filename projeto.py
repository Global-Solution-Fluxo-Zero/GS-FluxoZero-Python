print("\n\nBem-vindo a simulação de enchentes da Fluxo Zero™")
print("=================================================\n\n")

def menu_inicial():
    print("1 - Iniciar simulação.") # Acessa a simulação
    print("2 - Histórico de simulações anteriores.") # Acessa o json
    print("3 - Sair do programa.")
    escolha = input("\nEscolha uma opção: ")
    return escolha

def menu_simulacao():
    while True:
        print(":: Simulação de enchentes ::")
        print("\n")
        print("a. Configurar simulação.")
        print("b. Iniciar simulação.")
        print("c. Fechar simulação.")
        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "a":
                pass
            case "b":
                pass
            case "c":
                print("Fechando simulação...\n")
                break
            case _:
                print("Insira um valor válido!\n")



while True:
    opcao = menu_inicial()
    match opcao:
        case "1":
            print("Iniciando simulação...\n")
            menu_simulacao()
        case "2":
            print("Abrindo histórico da simulação...\n")
        case "3":
            print("Saindo do programa...\n")
            break
        case _:
            print("Insira um valor válido!\n")
