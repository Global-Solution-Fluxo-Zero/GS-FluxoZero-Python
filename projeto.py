print("\n\nBem-vindo a simulação de enchentes da Fluxo Zero™")
print("=================================================\n\n")

mm_chuva = None
hrs_chuva = None
tipo_solo = None
tipo_infiltracao = None
relevo_urbano_bool = None
eficiencia_drenagem = None
distancia_fluvial = None
obstrucao_bool = None

def simulacao_config():
    global mm_chuva
    global hrs_chuva
    global tipo_solo
    global tipo_infiltracao
    global relevo_urbano_bool
    global eficiencia_drenagem
    global distancia_fluvial
    global obstrucao_bool
    
    mm_chuva = float(input("Insira a quantidade de chuva prevista em mm: "))
    hrs_chuva = float(input("Insira quantas horas a chuva ira durar: "))
    tipo_solo = input("Tipo de solo do local observado (1 - Rochoso, 2 - Argiloso, 3 - Aluvial, 4 - Arenoso): ")
    tipo_infiltracao = input("Tipo de infiltração do solo (1 - Alta, 2 - Médio, 3 - Baixo): ")
    relevo_urbano_bool = input("O relevo é urbanizado? (1 - Sim, 2 - Não): ")
    eficiencia_drenagem = input("A eficiência de drenagem do local (1 - Eficiente, 2 - Moderada, 3 - Ineficiente, 4 - Inexistente): ")
    distancia_fluvial = float(input("Qual é a distância (em metros) de um rio ou lago do local onde você está?: "))
    obstrucao_bool = input("Há lixo, entulho, entupimentos em bueiros ou vias no local onde você está? (1 - Sim, 2 - Não): ")

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
        case "1":
            resposta[0] += 30
            resposta.append(1)
        case "2":
            resposta[0] += 20
            resposta.append(2)
        case "3":
            resposta[0] += 10
            resposta.append(3)
        case "4":
            resposta.append(4)
    
    match tipo_infiltracao:
        case "1":
            resposta.append(1)
        case "2":
            resposta[0] += 10
            resposta.append(2)
        case "3":
            resposta[0] += 20
            resposta.append(3)
     
    if relevo_urbano_bool == "1":
        resposta[0] += 20
        resposta.append(True)
    else:
        resposta.append(False)
    
    match eficiencia_drenagem:
        case "1":
            resposta.append(1)
        case "2":
            resposta[0] += 10
            resposta.append(2)
        case "3":
            resposta[0] += 20
            resposta.append(3)
        case "4":
            resposta[0] += 40
            resposta.append(4)

    if distancia_fluvial <= 250:
        resposta.append(1)
    else:    
        resposta[0] += 50
        resposta.append(2)

    if obstrucao_bool == "1":
        resposta[0] += 15
        resposta.append(True)
    else:
        resposta.append(False)

    return resposta

def simulacao_insight(resultado):
    if resultado[0] < 30:
        print("Risco muito baixo de alagamentos na situação atual.")
    elif resultado[0] < 50:
        print("Risco moderado — atenção a fatores locais.")
    elif resultado[0] < 70:
        print("Risco alto — possível ocorrência de alagamentos.")
    else:
        print("Risco muito alto — medidas preventivas são recomendadas imediatamente.")
    # Chuva
    print("\n")
    match resultado[1]:
        case 1:
            print("Chuva fraca (até 5 mm) — baixo risco de alagamentos isoladamente.")
            print("Preventivo: Ideal para verificar e manter o sistema de drenagem em dia; oportunidade para limpeza de bueiros.")

        case 2:
            print("Chuva leve a moderada (5–10 mm) — risco pequeno, mas pode causar acúmulo em áreas críticas ou com drenagem fraca.")
            print("Preventivo: Realizar inspeções preventivas em pontos de acúmulo; monitorar locais historicamente vulneráveis.")

        case 3:
            print("Chuva moderada a forte (10–25 mm) — risco elevado em áreas com drenagem insuficiente ou solo com baixa infiltração.")
            print("Pode causar alagamentos localizados, principalmente em regiões urbanas com pavimentação sem drenagem.")
            print("Preventivo: Ativar planos de contingência, garantir limpeza de bocas de lobo e alertar moradores de áreas de risco.")

        case 4:
            print("Chuva intensa (> 25 mm) — risco muito alto de alagamentos generalizados e enxurradas.")
            print("A combinação de intensidade e duração pode gerar transbordamentos de rios, escoamento superficial excessivo e deslizamentos.")
            print("Preventivo: Acionar defesa civil, emitir alertas preventivos, evacuar áreas críticas se necessário, e reforçar contenções.")
    # Tipo do Solo
    print("\n")
    match resultado[2]:
        case 1:
            print("Solo rochoso — infiltração muito baixa, a água escorre facilmente.")
            print("Aumenta o risco de enxurradas, principalmente em áreas inclinadas.")
            print("Preventivo: Criar canais de drenagem superficial bem definidos e vegetação de cobertura para desacelerar o escoamento.")
        case 2:
            print("Solo argiloso — infiltração baixa, acumula água com facilidade.")
            print("Propenso a alagamentos por saturação e escoamento lento.")
            print("Preventivo: Instalar trincheiras de infiltração e pavimentos drenantes; evitar impermeabilização excessiva.")
        case 3:
            print("Solo aluvial — infiltração geralmente alta, favorece a absorção da água.")
            print("Reduz o risco de alagamento se não houver obstruções ou drenagem inadequada.")
            print("Preventivo: Manter vegetação natural e preservar áreas alagáveis como zonas de amortecimento.")
        case 4:
            print("Solo arenoso — infiltração alta, a água penetra rapidamente no solo.")
            print("Baixo risco de alagamentos, mas pode afetar a estabilidade do solo em grandes volumes.")
            print("Preventivo: Monitorar a erosão em áreas inclinadas e combinar com barreiras vegetais para retenção.")
    # Infiltração do Solo
    print("\n")
    match resultado[3]:
        case 1:
            print("Infiltração alta — o solo absorve a água rapidamente.")
            print("Baixo risco de alagamentos relacionados à capacidade de absorção do solo.")
            print("Preventivo: Manter o solo permeável e evitar compactação com obras ou tráfego pesado.")
        case 2:
            print("Infiltração média — o solo absorve água em ritmo moderado.")
            print("Pode causar acúmulo de água em chuvas prolongadas ou intensas.")
            print("Preventivo: Instalar pavimentos permeáveis e aumentar áreas verdes para melhorar a absorção.")
        case 3:
            print("Infiltração baixa — o solo retém pouco a água, o que favorece o escoamento superficial.")
            print("Alto risco de alagamentos, principalmente se combinado com chuvas fortes e drenagem deficiente.")
            print("Preventivo: Implementar técnicas de infiltração como bacias de retenção, trincheiras e jardins de chuva.")
    # Relevo Urbanizado
    print("\n")
    match resultado[4]:
        case 1:
            print("Relevo urbanizado — há construções em regiões de inclinação.")
            print("A impermeabilização do solo reduz a infiltração e aumenta o escoamento superficial.")
            print("Em caso de chuvas fortes, há maior risco de enxurradas, alagamentos e até deslizamentos.")
            print("Preventivo: Implantar sistemas eficientes de drenagem, contenção de encostas e vegetação estabilizadora.")
        case 2:
            print("Relevo não urbanizado — a área mantém cobertura natural ou rural.")
            print("A presença de vegetação e solo permeável ajuda a absorver a água da chuva.")
            print("Preventivo: Preservar a vegetação nativa e evitar o desmatamento; manter o solo sem compactação excessiva.")
    # Drenagem
    print("\n")
    match resultado[5]:
        case 1:
            print("Drenagem eficiente — o local possui sistema de escoamento adequado.")
            print("Risco de alagamento é consideravelmente reduzido, mesmo em chuvas moderadas a fortes.")
            print("Preventivo: Manter a limpeza e a manutenção regular dos sistemas de drenagem para garantir a eficiência.")
        case 2:
            print("Drenagem moderada — o local tem algum sistema de escoamento, mas com limitações.")
            print("Pode haver acúmulo de água em chuvas mais intensas ou duradouras.")
            print("Preventivo: Avaliar pontos de gargalo, complementar com estruturas como bocas de lobo e valas de infiltração.")
        case 3:
            print("Drenagem ineficiente — o sistema é insuficiente para o volume de água.")
            print("Alto risco de alagamentos mesmo com chuvas moderadas.")
            print("Preventivo: Reestruturar o sistema de drenagem, instalar soluções como pavimento permeável e bacias de retenção.")
        case 4:
            print("Drenagem inexistente — não há infraestrutura para escoamento da água da chuva.")
            print("Altíssimo risco de alagamentos em qualquer chuva mais intensa.")
            print("Preventivo: Projetar e implantar um sistema de drenagem básico com canais, bueiros e áreas de absorção.")
    # Distância fluvial
    print("\n")
    if resultado[6] <= 250:
        print("Distância fluvial próxima (até 250 m).")
        print("Alto risco de alagamentos por transbordamento de rios ou lagos próximos.")
        print("Preventivo: Monitoramento constante do nível da água, uso de barreiras físicas e sistemas de alerta antecipado.")
    else:
        print("Distância fluvial segura (> 250 m).")
        print("Baixo risco de enchente direta por proximidade com rios ou lagos.")
        print("Preventivo: Mesmo em zonas mais distantes, mantenha sistemas de drenagem para evitar acúmulo de água por outras causas.")
    # Obstruções
    print("\n")
    match resultado[7]:
        case 1:
            print("Há obstruções (lixo, entulho ou entupimentos) em vias ou bueiros.")
            print("Risco muito alto de alagamentos, mesmo com chuvas fracas, devido ao bloqueio da drenagem.")
            print("Preventivo: Realizar limpeza imediata, campanhas de conscientização e inspeções frequentes em épocas de chuva.")
        case 2:
            print("Nenhuma obstrução visível em vias ou drenagens.")
            print("Boa condição para escoamento da água da chuva.")
            print("Preventivo: Manter a limpeza periódica e monitoramento, especialmente antes de períodos de chuva intensa.")
    print("\n")
    input("Aperte ENTER para continuar...\n")

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
                simulacao_config()
                #perguntar se quer salvar o historico com nova func
            case "b":
                print("Gerando resposta...\n")
                simulacao_insight(simulacao_calc(mm_chuva, hrs_chuva, tipo_solo, tipo_infiltracao, relevo_urbano_bool, eficiencia_drenagem, distancia_fluvial, obstrucao_bool))
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