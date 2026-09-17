# Dell LEAD - Introdução à Lógica de Programação em Python

Repositório dedicado ao desenvolvimento, implementação prática e versionamento dos projetos e oficinas do curso **Introdução à Lógica de Programação em Python**, promovido pelo **Dell LEAD** (Laboratório de Estudos em Aprendizagem e Desenvolvimento).

O curso aborda os conceitos fundamentais da lógica de programação e algoritmos utilizando a linguagem Python, englobando manipulação de variáveis, operadores aritméticos e relacionais, conversão e coerção de tipos, estruturas condicionais e de repetição, estruturas de dados nativas (listas, tuplas, conjuntos e dicionários aninhados), modularização através de funções com docstrings e passagem de parâmetros flexíveis, além dos princípios iniciais de Programação Orientada a Objetos (POO) e tratamento robusto de exceções.

---

## Estrutura do Repositório

```text
Dell LEAD Introdução à Lógica de Programação em Python/
├── Aula 1.2 - Atribuindo valores a variáveis corretamente/
├── Aula 1.5 - Laços de repetição/
├── Aula 2.2 - Listas para tudo/
├── Aula 2.4 - Conjuntos e suas utilizações/
├── Aula 2.5 - Dicionário e sua flexibilidade/
├── Aula 3.1 - Dividindo e reutilizando o código/
└── Aula 3.2 - Introdução a programação orientada a objetos/
```

---

## Oficinas Desenvolvidas

| Aula | Tema | Algoritmos / Ferramentas / Conceitos | Status |
| :--- | :--- | :--- | :---: |
| **Aula 1.2** | [Atribuindo valores a variáveis corretamente](./Aula%201.2%20-%20Atribuindo%20valores%20a%20variáveis%20corretamente) | Entrada com `input`, coerção de tipos (`float`, `str`), cálculo de IMC | Concluído |
| **Aula 1.5** | [Laços de repetição](./Aula%201.5%20-%20Laços%20de%20repetição) | Laço `for`, `range`, laço aninhado, operador módulo (`%`), controle de fluxo com `break` | Concluído |
| **Aula 2.2** | [Listas para tudo](./Aula%202.2%20-%20Listas%20para%20tudo) | Listas dinâmicas, `len`, `count`, `append`, `sorted`, indexação negativa, apuração estatística | Concluído |
| **Aula 2.4** | [Conjuntos e suas utilizações](./Aula%202.4%20-%20Conjuntos%20e%20suas%20utilizações) | Conjuntos (`set`), união (`\|`), interseção (`&`), diferença (`-`), cálculo de cobertura máxima | Concluído |
| **Aula 2.5** | [Dicionário e sua flexibilidade](./Aula%202.5%20-%20Dicionário%20e%20sua%20flexibilidade) | Dicionários aninhados, chave-valor dinâmico, ordenação alfabética com `sorted`, função `lambda` | Concluído |
| **Aula 3.1** | [Dividindo e reutilizando o código](./Aula%203.1%20-%20Dividindo%20e%20reutilizando%20o%20código) | Funções modulares, `docstrings`, desempacotamento de tuplas, parâmetros posicionais, nomeados e default | Concluído |
| **Aula 3.2** | [Introdução a programação orientada a objetos](./Aula%203.2%20-%20Introdução%20a%20programação%20orientada%20a%20objetos) | Classes e objetos, método especial `__str__`, métodos de instância, `try/except` e `raise Exception` | Concluído |

---

## Tecnologias e Recursos Utilizados

* **Linguagem:** Python 3.12+ (sem dependências externas, utilizando a biblioteca padrão)
* **Entrada e Saída:** `input()`, `print()`, interpolação com `.format()` e concatenação
* **Tipos de Dados Primitivos:** `int`, `float`, `str`, `bool`
* **Coleções e Estruturas de Dados:** `list`, `tuple`, `set`, `dict`
* **Controle de Fluxo:** `if`, `elif`, `else`, `while`, `for`, `break`
* **Funções e Modularização:** `def`, valores padrão, docstrings no padrão PEP 257, expressões `lambda`
* **Paradigma Orientado a Objetos:** Classes, construtor `__init__`, atributos de instância, representação textual `__str__`
* **Tratamento de Exceções:** `try`, `except`, `raise Exception`, `ValueError`
* **Ambiente de Execução:** Scripts Python (`.py`) executáveis via linha de comando

---

## Como Executar as Oficinas

### 1. Pré-requisitos
Certifique-se de possuir o Python 3 instalado no seu ambiente de desenvolvimento:
```powershell
python --version
```

### 2. Clonando o Repositório
```powershell
git clone https://github.com/pedrolabre/Dell-LEAD-Introducao-a-Logica-de-Programacao-em-Python.git
cd Dell-LEAD-Introducao-a-Logica-de-Programacao-em-Python
```

### 3. Executando uma Oficina
Você pode executar qualquer um dos scripts das oficinas diretamente pelo terminal, por exemplo:
```powershell
python "Aula 1.2 - Atribuindo valores a variáveis corretamente\oficina.py"
```
*(ou navegar até o diretório da aula correspondente e executar `python oficina.py`)*
