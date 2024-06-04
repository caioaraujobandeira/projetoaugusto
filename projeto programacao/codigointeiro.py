# Função para procurar o carro na lista
def procurar_carro(nome_carro, lista_carros):
    # Normaliza o nome do carro para garantir que a comparação não seja sensível a maiúsculas/minúsculas
    nome_carro = nome_carro.strip().lower()
    for carro in lista_carros:
        if carro.lower() == nome_carro:
            return "Carro encontrado!"
    return "Carro não encontrado!"

# Função para avaliar o carro com base no preço


def avaliacao_carro(preco):
    if preco < 10000:
        return "mal estado"
    elif preco < 30000:
        return "conservado"
    elif preco < 60000:
        return "seminovo"
    else:
        return "novo"


# Lista de carros
lista_carros = [
    "CarroA", "CarroB", "CarroC", "CarroD", "CarroE",
    "CarroF", "CarroG", "CarroH", "CarroI", "CarroJ"
]

# Imprime a lista de carros para depuração
print("Lista de carros disponíveis:")
print(lista_carros)

# Loop para interagir com o usuário
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
