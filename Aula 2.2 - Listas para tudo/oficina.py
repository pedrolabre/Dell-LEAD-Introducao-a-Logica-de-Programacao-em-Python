# Apresentação e definição dos dados da pesquisa
# Lista com os cursos disponíveis
cursos = [
    'Engenharia de Software',
    'Python para Data Science',
    'Introdução a Java'
]

# Lista com as respostas dos colegas (índices correspondentes aos cursos)
respostas = [
    1, 2, 0, 1, 1, 1, 1, 0, 0, 2, 2, 0, 1, 1,
    1, 1, 2, 0, 1, 1, 0, 1, 0, 2, 1, 1, 0, 2,
    2, 1, 0, 1, 1, 0, 0, 0, 1, 1, 2, 1
]

# Total de votos apurados usando a função nativa len()
total_votos = len(respostas)

# Exibição do cabeçalho e do total de votos
print("--- Resultado da Pesquisa de Cursos ---")
print("Total de votos apurados:", total_votos)
print("\nVotação por curso:")

# Lista para armazenar o número de votos de cada curso
votos = []

# Laço para contabilizar os votos de cada curso e calcular a porcentagem
for i in range(len(cursos)):
    qtd_votos = respostas.count(i)
    votos.append(qtd_votos)
    porcentagem = (qtd_votos / total_votos) * 100
    print("- " + cursos[i] + ":", qtd_votos, "votos (" + str(porcentagem) + "%)")

# Identificação do curso mais votado utilizando sorted(), indexação negativa [-1] e index()
votos_ordenados = sorted(votos)
maior_voto = votos_ordenados[-1]
indice_vencedor = votos.index(maior_voto)
curso_escolhido = cursos[indice_vencedor]

# Exibição do curso escolhido pela votação
print("\n--- Curso Escolhido ---")
print("O curso escolhido pela votação foi:", curso_escolhido)

input("\nPressione Enter para encerrar...")
