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

# Resumo dos dados cadastrados
print("\nCadastro concluído com sucesso!")
print("Total de gêneros registrados:", len(livraria))

input("\nPressione Enter para encerrar...")
