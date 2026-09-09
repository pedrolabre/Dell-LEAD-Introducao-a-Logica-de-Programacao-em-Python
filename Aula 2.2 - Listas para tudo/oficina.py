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

input("\nPressione Enter para encerrar...")
