# Aula 2.2 - Listas para tudo

Este módulo aborda o uso de listas dinâmicas em Python para coleta, contagem, manipulação estatística e ordenação de dados, aplicando funções embutidas como `len()`, métodos de lista como `.count()`, `.append()`, `.index()`, a função nativa `sorted()` e técnicas de indexação negativa para tomada de decisão automatizada.

---

## Objetivo da Aula
* Compreender o conceito de listas mutáveis e ordenadas em Python;
* Inicializar listas contendo dados categóricos e numéricos;
* Utilizar a função nativa `len()` para calcular o tamanho e o total de registros de uma coleção;
* Utilizar o método de lista `.count()` para quantificar a frequência absoluta de ocorrência de cada elemento;
* Calcular métricas relativas (porcentagens) com base no total acumulado;
* Ordenar coleções numéricas com a função `sorted()`;
* Aplicar indexação reversa (`[-1]`) para obter o maior elemento de uma sequência ordenada;
* Recuperar a posição de um valor na lista original através do método `.index()`.

---

## Enunciado da Oficina
> **Oficina Microlearning 7**
> 
> Olá, seja bem-vindo!
> 
> Você está pronto para praticar o que aprendeu nessa aula?
> 
> Para isso, imagine a seguinte situação:
> 
> Depois de se apaixonar por Programação e por Python, você ficou muito curioso com todo esse universo e quer fazer outro curso para se especializar ainda mais nessa área.
> 
> Como você é uma pessoa indecisa, pediu ajuda aos seus colegas programadores para decidir qual curso você faria. Dessa forma, você apresentou a eles uma lista contendo 3 cursos, conforme trecho a seguir:
> 
> ```python
> cursos = [
>     'Engenharia de Software',
>     'Python para Data Science',
>     'Introdução a Java'
> ]
> ```
> 
> Como seus colegas sabem que você gosta de programar, eles responderam apenas com o índice do curso que desejam que você curse. Assim, aqueles que querem que você faça ‘Engenharia de Software’ responderam 0, aqueles que desejam que você faça ‘Python para Data Science’ responderam 1 e os que querem ‘Introdução à Java’ responderam 2, conforme lista a seguir:
> 
> ```python
> respostas = [
>     1, 2, 0, 1, 1, 1, 1, 0, 0, 2, 2, 0, 1, 1,
>     1, 1, 2, 0, 1, 1, 0, 1, 0, 2, 1, 1, 0, 2,
>     2, 1, 0, 1, 1, 0, 0, 0, 1, 1, 2, 1
> ]
> ```
> 
> Agora, com tantos dados em mãos, para descobrir quais foram os resultados da pesquisa, você tem que construir um programa que apresente o número total e a porcentagem de votos para cada um dos cursos. Além disso, você deve apresentar qual curso foi o escolhido pela votação.
> 
> Então, chegou o momento de você praticar e resolver o problema proposto. Bons estudos!

---

## Conceitos e Técnicas Aplicadas
* **Estrutura de Listas (`list`)**: Armazenamento dos nomes dos cursos (`cursos`) e do histórico de votos dos participantes (`respostas`).
* **Função `len()`**: Contabilização instantânea do volume total de votos apurados ($N = 40$).
* **Método `.count(valor)`**: Varredura interna otimizada na lista de respostas para contar os votos de cada curso específico.
* **Cálculo Percentual**: Aplicação da fórmula matemática $\text{Porcentagem} = \left(\frac{\text{votos}}{\text{total}}\right) \times 100$.
* **Função `sorted()`**: Ordenação ascendente dos totais de votos para encontrar os extremos da distribuição.
* **Indexação Negativa (`[-1]`)**: Acesso direto ao último elemento da lista ordenada (correspondente ao maior número de votos).
* **Método `.index(valor)`**: Localização do índice posicional do vencedor na lista original para recuperar o nome do curso correspondente na lista `cursos`.

---

## Processo de Construção

O desenvolvimento da solução no arquivo [`oficina.py`](./oficina.py) foi estruturado em 4 etapas:

1. **Definição das Coleções de Dados:** Declaração da lista `cursos` com os 3 títulos disponíveis e da lista `respostas` com os 40 votos registrados.
2. **Apuração Geral de Votos:** Obtenção do total de participantes via `total_votos = len(respostas)` e impressão do cabeçalho.
3. **Contagem e Proporção por Curso:**
   * Laço `for i in range(len(cursos))` para percorrer cada curso disponível;
   * Uso de `respostas.count(i)` para apurar os votos do curso de índice `i`;
   * Inclusão do total em uma lista auxiliar `votos` via `.append()`;
   * Cálculo e impressão da porcentagem com concatenação de strings.
4. **Identificação do Curso Vencedor:**
   * Ordenação da lista de votos com `votos_ordenados = sorted(votos)`;
   * Extração do valor máximo através do índice negativo `maior_voto = votos_ordenados[-1]`;
   * Obtenção do índice original do ganhador com `votos.index(maior_voto)`;
   * Recuperação e exibição do nome do curso com `cursos[indice_vencedor]`.

---

## Resultados Obtidos

Ao executar o script `oficina.py`, o terminal apresenta a apuração consolidada da votação:

```text
--- Resultado da Pesquisa de Cursos ---
Total de votos apurados: 40

Votação por curso:
- Engenharia de Software: 12 votos (30.0%)
- Python para Data Science: 20 votos (50.0%)
- Introdução a Java: 8 votos (20.0%)

--- Curso Escolhido ---
O curso escolhido pela votação foi: Python para Data Science

Pressione Enter para encerrar...
```

**Análise dos Resultados:**
* O total de votos foi de **40 registros**, sem votos nulos ou inválidos.
* O curso **Python para Data Science** obteve a maioria absoluta dos votos: **20 votos**, correspondendo a exatamente **50.0%** da preferência dos entrevistados.
* **Engenharia de Software** ficou em segundo lugar com **12 votos** (30.0%) e **Introdução a Java** obteve **8 votos** (20.0%).
* O algoritmo identificou o curso vencedor de forma dinâmica e programática, dispensando estruturas manuais de decisão.

---

## Arquivos da Aula
* [`oficina.py`](./oficina.py): Código Python com o algoritmo completo de apuração estatística de listas.

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
python "Aula 2.2 - Listas para tudo\oficina.py"
```
*(ou navegue até a pasta da aula e execute `python oficina.py`)*
