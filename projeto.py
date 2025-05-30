print("\n\nBem-vindo a simulação de enchentes da Fluxo Zero™")
print("=================================================\n\n")

def simulacao_calc(
        mm_chuva,
        hrs_chuva,
        tipo_solo,
        tipo_infiltracao,
        relevo_urbano_bool,
        eficiencia_drenagem,
        distancia_fluvial,
        obstrucao_bool
        ):
    #[pontos, chuva_tipo, tipo_solo, 
    # tipo_infiltracao, relevo_urbano, sistema_drenagem,
    # distancia_rio, obstrucao]
    resposta = [0]
    chuva_mmhrs = mm_chuva/hrs_chuva

    if chuva_mmhrs <= 2.5:
        resposta.append(1)
    elif chuva_mmhrs > 2.5 and chuva_mmhrs <= 10:
        resposta[0] += 10
        resposta.append(2)
    elif chuva_mmhrs > 10 and chuva_mmhrs <= 50:
        resposta[0] += 20
        resposta.append(3)
    else:
        resposta[0] += 30
        resposta.append(4)

    match tipo_solo:
        case 1:
            resposta[0] *= 2
            resposta.append(1)
        case 2:
            resposta[0] += 20
            resposta.append(2)
        case 3:
            resposta[0] += 10
            resposta.append(3)
        case 4:
            resposta.append(4)
    
    match tipo_infiltracao:
        case 1:
            resposta[0] *= 1.5
            resposta.append(1)
        case 2:
            resposta[0] += 10
            resposta.append(2)
        case 3:
            resposta.append(3)
     
    if relevo_urbano_bool is True:
        resposta[0] += 20
        resposta.append(relevo_urbano_bool)
    else:
        resposta.append(relevo_urbano_bool)
    
    match eficiencia_drenagem:
        case 1:
            resposta.append(1)
        case 2:
            resposta[0] += 10
            resposta.append(2)
        case 3:
            resposta[0] += 20
            resposta.append(3)
        case 4:
            resposta[0] *= 2
            resposta.append(4)

    if distancia_fluvial < 100:
        resposta.append(1)
    else:    
        resposta[0] += 50
        resposta.append(2)

    if obstrucao_bool is True:
        resposta[0] *= 1.5
        resposta.append(obstrucao_bool)
    else:
        resposta.append(obstrucao_bool)

    return resposta

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

while True:
    opcao = menu_inicial()
    match opcao:
        case "1":
            print("Iniciando simulação...\n")
            menu_simulacao()
        case "2":
            print("Abrindo histórico da simulação...\n")
            menu_historico()
        case "3":
            print("Saindo do programa...\n")
            break
        case _:
            print("Insira um valor válido!")