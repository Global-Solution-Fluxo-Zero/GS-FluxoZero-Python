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
            print("Insira um valor válido!")


def menu_historico():
    while True:
        print(":: Histórico das enchentes ::")
        print("\n")
        print("a. Ver histórico.")
        print("b. Simular a partir de um histórico.")
        print("c. Apagar um histórico.")
        print("d. Fechar histórico.")
        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "a":
                # Mostrar todo o histórico de simulações
                print("Exibindo histórico de simulações...\n")
            case "b":
                # Simular a partir de um ID 
                digite_id = input("Digite o ID da simulação que deseja reproduzir: ")
                print(f"Reproduzindo simulação com ID: {digite_id}...\n")
                certeza_id = input("Você tem certeza que deseja reproduzir essa simulação? (1 - Sim, 2 - Não ): ")
                match certeza_id:
                    case "1":
                        print("Simulação reproduzida com sucesso!\n")
                    case "2":
                        print("Reprodução cancelada.\n")
                    case _:
                        print("Opção inválida. Retornando ao menu principal.\n")
                break
            case "c":
                print("Digie um ID para apagar o histórico: ")
                digite_id = input("Digite o ID da simulação que deseja apagar: ")
                print(f"Apagando simulação com ID: {digite_id}...\n")
                certeza_apagar = input("Você tem certeza que deseja apagar essa simulação? (1 - Sim, 2- Não ): ")
                match certeza_apagar:
                    case "1":
                        print("Simulação apagada com sucesso!\n")
                    case "2":
                        print("Apagamento cancelado.\n")
                        continue
                    case _:
                        print("Opção inválida. Retornando ao menu principal.\n")
            case "d":
                print("Fechando histórico...\n")
                break
            case _:
                print("Insira um valor válido!\n")

