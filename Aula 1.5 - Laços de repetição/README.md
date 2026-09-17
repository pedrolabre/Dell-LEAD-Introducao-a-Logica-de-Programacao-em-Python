# Aula 1.5 - Laços de repetição

Este módulo aborda as estruturas de controle de repetição em Python, explorando a utilização do laço `for`, geração de sequências numéricas iteráveis com a função `range()`, aninhamento de loops (*nested loops*), uso de variáveis sentinelas booleanas e comandos de interrupção de fluxo com `break` para a identificação eficiente de números primos.

---

## Objetivo da Aula
* Compreender o funcionamento das estruturas de repetição determinísticas (`for`);
* Utilizar a função nativa `range()` com limites inicial e final para controle de iterações;
* Implementar laços aninhados para problemas que exigem verificação combinatória elemento a elemento;
* Aplicar o operador aritmético módulo (`%`) para testar a divisibilidade exata entre números inteiros;
* Utilizar variáveis booleanas de controle (*flags*) para rastreamento de estados;
* Otimizar a execução do algoritmo utilizando a instrução `break` para interromper laços precocemente assim que uma condição de parada for satisfeita.

---

## Enunciado da Oficina
> **Oficina Microlearning 5**
> 
> Os números primos são números naturais maiores que 1 e que não são produtos de dois outros números naturais positivos, ou seja, são divisíveis apenas por 1 e por eles mesmos. Além disso, números primos são muito úteis em computação e despertam a curiosidade de matemáticos há séculos.
> 
> Como exemplo, tomemos o número 5, que é considerado um número primo porque não existe par de números entre 2 e 4 cuja multiplicação seja igual a 5. Já o 6 não é um número primo, pois existe um par entre 2 e 5 cujo resultado é igual a 6, o par é 2 e 3.
> 
> Para esta oficina, você vai usar uma definição diferente da que foi apresentada acima, mas ainda é uma definição equivalente. Antes disso, analise a seguinte situação: um número $X$ é primo se, para todo número $N$ entre 2 e $X - 1$, o resto da divisão entre $X$ e $N$ for diferente de 0.
> 
> Seguindo essa lógica, desenvolva um notebook Jupyter com um programa Python que apresente textualmente todos os números primos entre 2 e 100 (incluindo o valor 100). Com isso, seu programa deve percorrer todos os números nesse intervalo e testar individualmente cada um, vendo se ele é primo ou não. Caso o número seja primo, você deve imprimir o valor em tela. Caso não seja, deve simplesmente ignorá-lo.
> 
> Boa prática!

---

## Conceitos e Técnicas Aplicadas
* **Laço de Repetição (`for ... in range(...)`)**:
  * `range(2, 101)`: Cria uma sequência iterável de inteiros começando em 2 e terminando em 100 (limite superior exclusivo no Python).
  * `range(2, numero)`: Gera os divisores candidatos para testar a primalidade do número atual.
* **Operador Módulo (`%`)**: Verifica o resto da divisão inteira. Quando `numero % divisor == 0`, constata-se que o número não é primo.
* **Sentinela Booleana (`eh_primo`)**: Variável inicializada como `True` a cada ciclo e alterada para `False` se algum divisor for identificado.
* **Instrução `break`**: Interrompe o laço interno no primeiro divisor encontrado, evitando iterações desnecessárias e otimizando a performance do algoritmo.
* **Estrutura Condicional (`if eh_primo`)**: Filtra e imprime somente os valores que mantiveram a condição de primalidade após o término do laço interno.

---

## Processo de Construção

O desenvolvimento da solução no arquivo [`oficina.py`](./oficina.py) foi estruturado nas seguintes etapas:

1. **Apresentação Inicial:** Impressão do cabeçalho indicativo do programa no console.
2. **Laço Principal de Varredura:** Inicialização do loop `for numero in range(2, 101)` para inspecionar sequencialmente cada inteiro de 2 a 100.
3. **Definição do Estado Inicial:** Atribuição da sentinela `eh_primo = True` para cada número avaliado.
4. **Laço Aninhado de Verificação de Divisibilidade:** Execução de `for divisor in range(2, numero)` para testar se há divisão exata (`numero % divisor == 0`).
5. **Otimização de Fluxo:** Atribuição de `eh_primo = False` e execução imediata de `break` ao identificar qualquer divisor exato.
6. **Exibição dos Primos:** Avaliação do predicado booleano `if eh_primo:` e impressão do número em tela.

---

## Resultados Obtidos

Ao executar o script `oficina.py`, o terminal apresenta a listagem completa dos 25 números primos compreendidos entre 2 e 100:

```text
Números primos entre 2 e 100:
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97

Pressione Enter para encerrar...
```

**Análise dos Resultados:**
* O programa identificou com precisão matemática os **25 números primos** existentes entre 2 e 100.
* Números compostos conhecidos (como 4, 9, 15, 49, 91) foram descartados imediatamente graças ao operador módulo e ao comando `break`, que interrompe o laço interno sem realizar verificações redundantes.
* O número 2 (único número par primo) foi avaliado e exibido corretamente, já que o intervalo `range(2, 2)` é vazio, mantendo o valor booleano inicial `True`.

---

## Arquivos da Aula
* [`oficina.py`](./oficina.py): Código Python com a lógica de laços aninhados para detecção de números primos.

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
python "Aula 1.5 - Laços de repetição\oficina.py"
```
*(ou navegue até a pasta da aula e execute `python oficina.py`)*
