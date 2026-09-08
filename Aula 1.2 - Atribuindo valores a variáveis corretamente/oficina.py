# Entrada de dados do usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
peso = input("Digite seu peso (em kg): ")
altura = input("Digite sua altura (em metros, ex: 1.75): ")

# Conversão de tipos de dados
peso_float = float(peso)
altura_float = float(altura)

# Processamento: cálculo do IMC
altura_ao_quadrado = altura_float * altura_float
imc = peso_float / altura_ao_quadrado

# Conversão para string e saída formatada (desafio da oficina)
imc_str = str(imc)
print("\n" + nome + ", o seu IMC calculado é: " + imc_str)

input("\nPressione Enter para encerrar...")