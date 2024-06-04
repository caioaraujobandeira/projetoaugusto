# Questão 07
def avaliacao_carro(preco):
    if preco < 10000:
        return "mal estado"
    elif preco < 30000:
        return "conservado"
    elif preco < 60000:
        return "seminovo"
    else:
        return "novo"


mensagem_qualidade = avaliacao_carro(preco_carro)
print(mensagem_qualidade)
