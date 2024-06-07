def procurar_carro(nome_carro, lista_carros):
    nome_carro = nome_carro.strip().lower()
    for carro in lista_carros:
        if carro.lower() == nome_carro:
            return "Carro encontrado!"
    return "Carro não encontrado!"


def avaliacao_carro(preco):
    if preco < 10000:
        return "mal estado"
    elif preco < 30000:
        return "conservado"
    elif preco < 60000:
        return "seminovo"
    else:
        return "novo"

lista_carros = [
    "fiat", "mustang", "mercedes", "argo", "jeep",
    "ferrari", "pajero", "duster", "onix", "gol"
]

print("Lista de carros disponíveis:")
print(lista_carros)

continuar = 's'
while continuar.lower() == 's':
    nome_carro = input("Digite o nome do carro que você deseja comprar: ")
    preco_carro = float(
        input("Digite o valor do carro que você gostaria de pagar: "))

    print(
        f"O usuário gostaria de saber se o carro {nome_carro} está disponível e gostaria de pagar {preco_carro} reais nesse carro.")

    mensagem_carro = procurar_carro(nome_carro, lista_carros)
    print(mensagem_carro)

    mensagem_qualidade = avaliacao_carro(preco_carro)
    print(mensagem_qualidade)

    if mensagem_carro == "Carro encontrado!":
        qualidade_carro = mensagem_qualidade
        print(
            f"O usuário gostaria de um carro {nome_carro} na qualidade de {qualidade_carro}.")
        print(
            f"O valor do {nome_carro} é {preco_carro}. Já o valor da {qualidade_carro} é {preco_carro}.")

    # Perguntando se o usuário quer continuar
    continuar = input("Você quer continuar? (s/n): ")
