# Apresentação e definição dos dados do casamento
# Conjunto com todos os presentes desejados pelo casal
presentes = {
    'Cafeteira',
    'Micro-ondas',
    'Faqueiro',
    'Jogo de Toalhas',
    'Jogo de Panelas',
    'Liquidificador',
    'Torradeira',
    'Batedeira',
    'Aspirador de Pó',
    'Air Fryer',
    'Ferro de Passar',
    'Jogo de Cama'
}

# Catálogo de presentes oferecidos por cada uma das 4 lojas pesquisadas
loja1 = {
    'Cafeteira',
    'Micro-ondas',
    'Faqueiro',
    'Jogo de Panelas',
    'Liquidificador',
    'Jogo de Toalhas'
}

loja2 = {
    'Cafeteira',
    'Micro-ondas',
    'Batedeira',
    'Jogo de Panelas',
    'Torradeira',
    'Jogo de Toalhas'
}

loja3 = {
    'Cafeteira',
    'Micro-ondas',
    'Aspirador de Pó',
    'Jogo de Panelas',
    'Liquidificador'
}

loja4 = {
    'Cafeteira',
    'Micro-ondas',
    'Air Fryer',
    'Liquidificador',
    'Torradeira'
}

# Exibição do cabeçalho e total de presentes desejados
print("--- Planejamento de Presentes de Casamento ---")
print("Total de presentes desejados:", len(presentes))
print("Conjunto de presentes:", presentes)

# 1. Produtos oferecidos em ao menos uma loja (união dos conjuntos de todas as lojas)
ao_menos_uma = loja1 | loja2 | loja3 | loja4

# 2. Produtos oferecidos em todas as lojas (interseção dos conjuntos de todas as lojas)
todas_as_lojas = loja1 & loja2 & loja3 & loja4

# 3. Produtos não encontrados em nenhuma loja (diferença entre os presentes e os disponíveis)
nenhuma_loja = presentes - ao_menos_uma

# Exibição das respostas para as perguntas 1, 2 e 3
print("\n1. Produtos oferecidos em ao menos uma loja:")
print(ao_menos_uma)

print("\n2. Produtos oferecidos em todas as lojas:")
print(todas_as_lojas)

print("\n3. Produtos não encontrados em nenhuma loja:")
print(nenhuma_loja)

# 4. Produtos exclusivos de cada loja (diferença entre cada loja e a união das demais)
exclusivos_loja1 = loja1 - (loja2 | loja3 | loja4)
exclusivos_loja2 = loja2 - (loja1 | loja3 | loja4)
exclusivos_loja3 = loja3 - (loja1 | loja2 | loja4)
exclusivos_loja4 = loja4 - (loja1 | loja2 | loja3)

# Lista reunindo as coleções de itens exclusivos por loja
exclusivos_por_loja = [
    exclusivos_loja1,
    exclusivos_loja2,
    exclusivos_loja3,
    exclusivos_loja4
]

print("\n4. Produtos exclusivos de cada loja:")
for i in range(len(exclusivos_por_loja)):
    print("- Loja " + str(i + 1) + ":", exclusivos_por_loja[i])

# 5. Maior quantidade de presentes possíveis combinando duas lojas
# Cálculo do número de itens únicos (união) para cada par de lojas
coberturas_duas_lojas = [
    len(loja1 | loja2),
    len(loja1 | loja3),
    len(loja1 | loja4),
    len(loja2 | loja3),
    len(loja2 | loja4),
    len(loja3 | loja4)
]

# Obtenção da quantidade máxima utilizando a função max()
melhor_cobertura = max(coberturas_duas_lojas)

print("\n5. Maior quantidade de presentes cobertos escolhendo duas lojas:")
print(melhor_cobertura, "presentes")

input("\nPressione Enter para encerrar...")
