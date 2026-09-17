# Aula 1.2 - Atribuindo valores a variáveis corretamente

Este módulo introduz os fundamentos da manipulação de variáveis, captura de dados do usuário via console, conversão e coerção de tipos de dados primitivos (*type casting*) e execução de operações aritméticas para a resolução de problemas práticos no ecossistema Python.

---

## Objetivo da Aula
* Compreender a tipagem dinâmica e a atribuição de valores a variáveis em Python;
* Utilizar a função nativa `input()` para capturar dados digitados pelo usuário via terminal;
* Reconhecer que toda entrada capturada por `input()` é originalmente tratada como string (`str`);
* Realizar conversões de tipos primitivos utilizando as funções construtoras `float()` e `str()`;
* Executar cálculos aritméticos utilizando operadores matemáticos de multiplicação (`*`) e divisão (`/`);
* Formatar e exibir mensagens no console combinando texto e variáveis através de concatenação (`+`).

---

## Enunciado da Oficina
> **Oficina Microlearning 2**
> 
> Durante a aula, você aprendeu como fazer entrada e saída de dados, além de como ler strings e convertê-los para números. Nesta oficina, você deve construir um programa Python que faz a leitura do nome, da idade, do peso e da altura de uma pessoa, e calcula o Índice de Massa Corporal (IMC) dela. O IMC é uma medida internacionalmente aceita, que calcula se uma pessoa pode ter problemas de peso ou não. Sabendo disso, o IMC é calculado da seguinte forma:
> 
> $$\text{IMC} = \frac{\text{peso}}{\text{altura} \times \text{altura}}$$
> ou
> $$\text{IMC} = \frac{\text{peso}}{\text{altura}^2}$$
> 
> Ambas as fórmulas são iguais. Dessa forma, seu programa vai ajudar os usuários a calcularem o IMC deles. Ele deve receber como entrada de dados, o nome da pessoa, o peso e a altura. Depois, ele deve calcular o IMC e apresentar este valor na tela para o usuário. Logo abaixo está o cálculo do IMC já pronto para você utilizá-lo. Assumindo que as variáveis com os valores numéricos de peso e altura foram nomeadas como `peso_float` e `altura_float`, o código para calcular o IMC é:
> 
> ```python
> altura_ao_quadrado = altura_float * altura_float
> imc = peso_float / altura_ao_quadrado
> ```
> 
> Após este cálculo, imprima uma linha contendo o IMC da pessoa.
> 
> **DESAFIO:** foi discutido em aula como converter de uma string, ou seja, o tipo `str`, para um `float`. Como fazer o caminho inverso, converter de um `float` para `str`? Reflita um pouco e tente não só apresentar o valor numérico como escrever algum texto que auxilie a leitura do usuário.

---

## Conceitos e Técnicas Aplicadas
* **Entrada de Dados (`input`)**: Interação com o usuário via terminal para obtenção dos dados cadastrais (nome, idade, peso e altura).
* **Coerção de Tipos (*Casting*)**:
  * `float(peso)` e `float(altura)`: Conversão de strings com dados textuais para números de ponto flutuante aptos a operações aritméticas.
  * `str(imc)`: Conversão explícita de número float para texto para atender à exigência de concatenação de strings.
* **Operadores Aritméticos**:
  * Multiplicação (`*`): Cálculo da altura ao quadrado (`altura_float * altura_float`).
  * Divisão (`/`): Razão entre o peso e a altura elevada ao quadrado.
* **Concatenação de Strings (`+`)**: Junção fluida de literais de texto e variáveis string na função `print()`.

---

## Processo de Construção

O desenvolvimento da solução no arquivo [`oficina.py`](./oficina.py) foi estruturado em 4 etapas:

1. **Entrada de Dados:** Leitura das variáveis `nome`, `idade`, `peso` e `altura` fornecidas pelo usuário através de chamadas consecutivas à função `input()`.
2. **Conversão de Tipos:** Transformação de `peso` e `altura` para o tipo `float`, garantindo a precisão numérica necessária para os cálculos com decimais.
3. **Processamento do IMC:** Multiplicação da altura por si mesma para obter a área e divisão do peso pela altura ao quadrado para apuração do índice corporal.
4. **Conversão e Saída Formatada:** Transformação do valor float do IMC em string (`str(imc)`) e exibição no terminal da mensagem formatada com concatenação de strings.

---

## Resultados Obtidos

Ao executar o script `oficina.py` e fornecer os dados de entrada, o terminal apresenta a seguinte interação:

```text
Digite seu nome: Pedro Labre
Digite sua idade: 25
Digite seu peso (em kg): 75
Digite sua altura (em metros, ex: 1.75): 1.75

Pedro Labre, o seu IMC calculado é: 24.489795918367346

Pressione Enter para encerrar...
```

**Análise dos Resultados:**
* Para uma pessoa com **75 kg** e **1.75 m** de altura, o valor de $\text{altura}^2$ resulta em $3.0625$.
* O cálculo da divisão $\frac{75}{3.0625}$ entrega precisamente o IMC de **24.49**, classificado dentro da faixa de peso saudável segundo a Organização Mundial da Saúde (OMS).
* A conversão explícita para string garantiu a exibição correta via operador `+` sem gerar erros de tipo (`TypeError`).

---

## Arquivos da Aula
* [`oficina.py`](./oficina.py): Código Python com a implementação do cálculo interativo de IMC.

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
python "Aula 1.2 - Atribuindo valores a variáveis corretamente\oficina.py"
```
*(ou navegue até a pasta da aula e execute `python oficina.py`)*
