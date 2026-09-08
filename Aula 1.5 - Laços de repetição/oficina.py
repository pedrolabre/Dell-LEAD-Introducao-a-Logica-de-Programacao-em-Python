# Apresentação do programa
print("Números primos entre 2 e 100:")

# Laço principal: percorre todos os números no intervalo de 2 a 100 (inclusive)
for numero in range(2, 101):
    eh_primo = True

    # Laço aninhado: verifica se existe algum divisor entre 2 e numero - 1
    for divisor in range(2, numero):
        if numero % divisor == 0:
            eh_primo = False
            break  # Interrompe o laço interno assim que encontra um divisor

    # Se for primo, exibe o valor em tela; caso contrário, ignora
    if eh_primo:
        print(numero)

input("\nPressione Enter para encerrar...")
