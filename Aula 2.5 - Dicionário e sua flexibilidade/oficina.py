# Módulo de cadastro e leitura de dados dos livros
# Estrutura principal: dicionário aninhado (gênero -> subgênero -> lista de livros)
livraria = {}

print("--- Sistema de Gerenciamento da Livraria ---")
print("Módulo de Leitura e Cadastro de Livros")

# Laço para leitura iterativa dos dados dos livros
while True:
    print("\nPreencha os dados do livro:")
    titulo = input("Título: ")
    genero = input("Gênero: ")
    subgenero = input("Subgênero: ")
    editora = input("Editora: ")
    copias = int(input("Número de cópias em loja: "))
    valor = float(input("Valor (em R$): "))

    # Criação do dicionário com as informações do livro
    livro = {
        'titulo': titulo,
        'editora': editora,
        'copias': copias,
        'valor': valor
    }

    # Estruturação no dicionário aninhado por gênero e subgênero
    if genero not in livraria:
        livraria[genero] = {}

    if subgenero not in livraria[genero]:
        livraria[genero][subgenero] = []

    livraria[genero][subgenero].append(livro)

    # Verificação de continuidade do cadastro
    continuar = input("\nDeseja cadastrar outro livro? (s/n): ")
    if continuar.lower() != 's':
        break

# Módulo de apresentação dos livros disponíveis em loja
print("\n--- Apresentação dos Livros Disponíveis em Loja ---")

if len(livraria) == 0:
    print("\nNenhum livro foi cadastrado na livraria.")
else:
    # Apresentação dos gêneros em ordem alfabética
    for genero in sorted(livraria):
        print("\n--- {} ---".format(genero))

        # Apresentação dos subgêneros em ordem alfabética
        for subgenero in sorted(livraria[genero]):
            print("\n------ {} ------\n".format(subgenero))

            # Ordenação dos livros pela quantidade disponível em loja com função lambda
            livros_ordenados = sorted(livraria[genero][subgenero], key=lambda livro: livro['copias'])

            # Exibição detalhada de cada livro ordenado por quantidade
            for livro in livros_ordenados:
                print("Título: {} | Editora: {} | Cópias em loja: {} | Valor: R$ {:.2f}\n".format(
                    livro['titulo'],
                    livro['editora'],
                    livro['copias'],
                    livro['valor']
                ))

input("\nPressione Enter para encerrar...")
