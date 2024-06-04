# Questão 09
continuar = 's'
while continuar.lower() == 's':
    # Recebendo os dados do usuário
    nome_carro = input("Digite o nome do carro que você deseja comprar: ")
    preco_carro = float(
        input("Digite o valor do carro que você gostaria de pagar: "))

    # Exibindo a mensagem com os dados recebidos
    print(
        f"O usuário gostaria de saber se o carro {nome_carro} está disponível e gostaria de pagar {preco_carro} reais nesse carro.")

    # Procurando o carro na lista
    mensagem_carro = procurar_carro(nome_carro, lista_carros)
    print(mensagem_carro)

    # Avaliando o carro com base no preço
    mensagem_qualidade = avaliacao_carro(preco_carro)
    print(mensagem_qualidade)

    # Verificando disponibilidade e qualidade
    if mensagem_carro == "Carro encontrado!":
        qualidade_carro = mensagem_qualidade
        print(
            f"O usuário gostaria de um carro {nome_carro} na qualidade de {qualidade_carro}.")
        print(
            f"O valor do {nome_carro} é {preco_carro}. Já o valor da {qualidade_carro} é {preco_carro}.")

    # Perguntando se o usuário quer continuar
    continuar = input("Você quer continuar? (s/n): ")
