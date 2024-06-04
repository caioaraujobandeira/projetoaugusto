# Questão 06
def procurar_carro(nome_carro, lista_carros):
    nome_carro = nome_carro.strip().lower()
    for carro in lista_carros:
        if carro.lower() == nome_carro:
            return "Carro encontrado!"
    return "Carro não encontrado!"


mensagem_carro = procurar_carro(nome_carro, lista_carros)
print(mensagem_carro)
