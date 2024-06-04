# Questão 04
carro_encontrado = False
nome_carro_normalizado = nome_carro.strip().lower()
for carro in lista_carros:
    if carro.lower() == nome_carro_normalizado:
        print("Carro encontrado!")
        carro_encontrado = True
        break

if not carro_encontrado:
    print("Carro não encontrado!")
