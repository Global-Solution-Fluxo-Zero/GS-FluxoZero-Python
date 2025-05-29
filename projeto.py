print("\n\nBem-vindo a simulação de enchentes da Fluxo Zero™")
print("================================================\n\n")

def menu():
    print("\n")
    print("1 - Iniciar simulação.") # Acessa a simulação
    print("2 - Histórico de simulações anteriores.") # Acessa o json
    print("3 - Sair do programa.")
    escolha = input("\nEscolha uma opção:")
    return escolha

while True:
    opcao = menu()
    match opcao:
        case "1":
            print("Iniciando simulação...")
        case "2":
            print("Abrindo histórico da simulação...")
        case "3":
            print("Saindo do programa...")
            break
        case _:
            print("Insira um valor válido!")
