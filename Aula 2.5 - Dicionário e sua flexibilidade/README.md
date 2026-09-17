# Aula 2.5 - Dicionário e sua flexibilidade

Este módulo aborda o uso de dicionários (`dict`) em Python, explorando a criação de estruturas de dados hierárquicas e aninhadas (*nested dictionaries*), associação dinâmica de chaves e valores, iteração e ordenação de chaves com a função nativa `sorted()`, e classificação customizada de listas de dicionários por atributos numéricos utilizando funções anônimas (`lambda`).

---

## Objetivo da Aula
* Compreender a estrutura de dados dicionário (`dict`) baseada no modelo de pares chave-valor (*key-value*);
* Modelar dados complexos do mundo real através de dicionários aninhados em múltiplos níveis de hierarquia;
* Manipular e incluir registros dinamicamente testando a existência prévia de chaves com o operador `not in`;
* Construir laços iterativos com `while True` para cadastro contínuo de itens;
* Iterar sobre as chaves de um dicionário aplicando ordenação alfabética com a função `sorted()`;
* Ordenar coleções de objetos dicionários com base em um campo numérico específico utilizando o parâmetro `key` e expressões `lambda`;
* Formatar valores monetários e strings utilizando o método `.format()`.

---

## Enunciado da Oficina
> **Oficina Microlearning 10**
> 
> Durante a aula, você foi apresentado à criação de dicionários em diversas situações. Então, chegou o momento de praticar, a partir do que você aprendeu, e utilizar dicionários como estrutura básica para resolver o seguinte problema:
> 
> Imagine que você foi contratado para construir o sistema de gerenciamento de uma livraria e é o responsável por criar um módulo/célula, que fará a leitura dos dados de livros, que serão título, gênero, subgênero, editora, número de cópias em loja e valor em reais. Além disso, você também é o responsável pelo módulo de apresentação dos livros disponíveis em loja, de acordo com a seguinte organização: ao apresentar todos os livros disponíveis, eles devem ser separados, primeiro, por gênero e depois por subgênero, seguindo a estrutura a seguir:
> 
> ```text
> --- Gênero A ---
> 
> ------ Subgênero A.1 ------
> 
> Livro 01
> 
> Livro 02
> 
> ------ Subgênero A.2 ------
> 
> Livro 03
> 
> --- Gênero B ---
> 
> ------ Subgênero B.1 ------
> 
> Livro 04
> 
> ------ Subgênero B.2 ------
> 
> Livro 05
> 
> Livro 06
> ```
> 
> Tanto gênero quanto subgênero devem seguir uma ordem alfabética de apresentação, em que, dentro de um subgênero, os livros devem ser listados pela quantidade disponível em loja. Vamos lá?

---

## Conceitos e Técnicas Aplicadas
* **Dicionários Aninhados (`dict`)**: Estrutura `livraria[genero][subgenero] = [livro_1, livro_2, ...]`, permitindo indexação multinível e navegação hierárquica limpa.
* **Operador de Pertinência (`not in`)**: Garante que uma chave de gênero ou subgênero seja inicializada sem sobrescrever os dados já existentes (`if genero not in livraria: livraria[genero] = {}`).
* **Laço de Repetição com Sentinela (`while True` e `break`)**: Controle de fluxo que permite ao atendente cadastrar livros continuamente até digitar `"n"`.
* **Função `sorted()`**:
  * `sorted(livraria)`: Ordena lexicograficamente os gêneros principais.
  * `sorted(livraria[genero])`: Ordena lexicograficamente os subgêneros dentro de cada categoria.
* **Função Lambda (`lambda`)**:
  * `sorted(..., key=lambda livro: livro['copias'])`: Passagem de função customizada para instruir o Python a ordenar os livros com base no valor da chave `'copias'`.
* **Formatação Textual (`.format()`)**: Exibição elegante dos dados e controle de casas decimais para moeda (`R$ {:.2f}`).

---

## Processo de Construção

O desenvolvimento da solução no arquivo [`oficina.py`](./oficina.py) foi estruturado nas seguintes etapas:

1. **Estruturação Inicial:** Inicialização do dicionário vazio `livraria = {}` e exibição do cabeçalho do módulo.
2. **Entrada de Dados e Montagem do Objeto Livro:** Leitura interativa das variáveis `titulo`, `genero`, `subgenero`, `editora`, `copias` e `valor`, instanciando o dicionário `livro`.
3. **Aninhamento Hierárquico Seguro:**
   * Verificação e criação do gênero (`if genero not in livraria: livraria[genero] = {}`);
   * Verificação e criação do subgênero (`if subgenero not in livraria[genero]: livraria[genero][subgenero] = []`);
   * Inclusão do livro na lista correspondente via `.append(livro)`.
4. **Controle de Encerramento do Cadastro:** Avaliação da resposta `s/n` para definir a quebra do laço `while` via `break`.
5. **Módulo de Exibição com Ordenação Dupla:**
   * Laço externo percorrendo `sorted(livraria)` para os gêneros;
   * Laço intermediário percorrendo `sorted(livraria[genero])` para os subgêneros;
   * Ordenação da lista de livros por cópias com `sorted(..., key=lambda x: x['copias'])`;
   * Laço interno imprimindo cada livro devidamente formatado.

---

## Resultados Obtidos

Ao executar o script `oficina.py` e cadastrar três títulos de exemplo no acervo, o terminal apresenta a seguinte exibição hierárquica e ordenada:

```text
--- Sistema de Gerenciamento da Livraria ---
Módulo de Leitura e Cadastro de Livros

Preencha os dados do livro:
Título: Dom Casmurro
Gênero: Ficção
Subgênero: Romance
Editora: Principis
Número de cópias em loja: 5
Valor (em R$): 19.90

Deseja cadastrar outro livro? (s/n): s

Preencha os dados do livro:
Título: O Hobbit
Gênero: Ficção
Subgênero: Fantasia
Editora: HarperCollins
Número de cópias em loja: 12
Valor (em R$): 49.90

Deseja cadastrar outro livro? (s/n): s

Preencha os dados do livro:
Título: 1984
Gênero: Ficção
Subgênero: Ficção Científica
Editora: Companhia das Letras
Número de cópias em loja: 8
Valor (em R$): 39.90

Deseja cadastrar outro livro? (s/n): n

--- Apresentação dos Livros Disponíveis em Loja ---

--- Ficção ---

------ Fantasia ------

Título: O Hobbit | Editora: HarperCollins | Cópias em loja: 12 | Valor: R$ 49.90


------ Ficção Científica ------

Título: 1984 | Editora: Companhia das Letras | Cópias em loja: 8 | Valor: R$ 39.90


------ Romance ------

Título: Dom Casmurro | Editora: Principis | Cópias em loja: 5 | Valor: R$ 19.90


Pressione Enter para encerrar...
```

**Análise dos Resultados:**
* A hierarquia de dados foi mantida fielmente sem duplicidade de chaves.
* Os subgêneros foram apresentados em estrita ordem alfabética: **Fantasia**, depois **Ficção Científica** e por fim **Romance**.
* A ordenação interna por cópias garantiu que títulos com menor disponibilidade aparecessem primeiro, permitindo uma visualização imediata da reposição de estoque necessária.

---

## Arquivos da Aula
* [`oficina.py`](./oficina.py): Código Python com a implementação do sistema de catalogação e ordenação da livraria.

---

## Como Executar

### 1. Pré-requisitos
Certifique-se de ter o Python 3 instalado no seu ambiente:
```powershell
python --version
```

### 2. Executando o script Python
Na raiz do repositório:
```powershell
python "Aula 2.5 - Dicionário e sua flexibilidade\oficina.py"
```
*(ou navegue até a pasta da aula e execute `python oficina.py`)*
