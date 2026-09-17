# Aula 2.4 - Conjuntos e suas utilizações

Este módulo aborda a estrutura de dados de conjuntos (`set`) em Python e a aplicação prática da Teoria dos Conjuntos para resolução de problemas de disponibilidade de produtos, cálculo de união, interseção e diferença de dados, detecção de elementos exclusivos e otimização combinatória para cobertura de itens.

---

## Objetivo da Aula
* Compreender a natureza dos conjuntos (`set`) em Python (coleções não ordenadas, mutáveis e com garantia de elementos únicos);
* Inicializar conjuntos através da sintaxe literal `{item1, item2, ...}`;
* Aplicar a operação de **União** (`|`) para consolidar elementos presentes em ao menos um conjunto;
* Aplicar a operação de **Interseção** (`&`) para identificar elementos comuns compartilhados por múltiplos conjuntos simultaneamente;
* Aplicar a operação de **Diferença** (`-`) para encontrar itens presentes em um conjunto e ausentes em outro;
* Combinar operadores de conjuntos para determinar elementos exclusivos e calcular a combinação ótima de dois fornecedores.

---

## Enunciado da Oficina
> **Oficina Microlearning 9**
> 
> Nesta oficina, leia o seguinte caso, em seguida, faça o que se pede.
> 
> Suponha que você esteja ajudando um casal de amigos a planejar uma festa de casamento. Eles pediram para você montar a lista de presentes e, em seguida, pesquisar por lojas de departamento que trabalhem com esse tipo de lista. Você encontrou 4 lojas favoráveis, mas cada uma oferece apenas alguns dos presentes que o casal gostaria de ganhar. Como não dá para colocar a lista em todas as lojas ao mesmo tempo, você pode considerar algumas perguntas para ajudar nessa decisão, por exemplo:
> 
> 1. Quais produtos são oferecidos em ao menos uma loja?
> 2. Quais produtos são oferecidos em todas as lojas?
> 3. Quais produtos não são encontrados em nenhuma loja?
> 4. Quais produtos são exclusivos de cada loja?
> 5. Se for possível escolher duas lojas para cobrir o maior número de presentes, qual é a quantidade de presentes possíveis para cobrir dessa forma?
> 
> Com base no que você aprendeu durante os seus estudos, para esta oficina, você deve desenvolver um programa que calcule e imprima as respostas para essas perguntas.
> 
> Para isso, você pode utilizar os valores de exemplo para a lista de presentes, além dos catálogos das lojas:
> * **Lista de Presentes do Casal:** Cafeteira, Micro-ondas, Faqueiro, Jogo de Toalhas, Jogo de Panelas, Liquidificador, Torradeira, Batedeira, Aspirador de Pó, Air Fryer, Ferro de Passar, Jogo de Cama.
> * **Loja 1:** Cafeteira, Micro-ondas, Faqueiro, Jogo de Panelas, Liquidificador, Jogo de Toalhas.
> * **Loja 2:** Cafeteira, Micro-ondas, Batedeira, Jogo de Panelas, Torradeira, Jogo de Toalhas.
> * **Loja 3:** Cafeteira, Micro-ondas, Aspirador de Pó, Jogo de Panelas, Liquidificador.
> * **Loja 4:** Cafeteira, Micro-ondas, Air Fryer, Liquidificador, Torradeira.
> 
> Bem, lá vão algumas dicas para te ajudar: as três primeiras perguntas podem ser respondidas imprimindo conjuntos ou listas com os produtos correspondentes, a quarta pergunta pode ser respondida imprimindo uma lista de quatro coleções de produtos ou imprimindo uma coleção por linha, a quinta pergunta pode ser respondida apenas com o número de presentes da melhor combinação de lojas, não precisa dizer qual é a combinação.
> 
> Agora é hora de praticar o que você aprendeu e ajudar o casal de amigos.
> 
> Bom desempenho!

---

## Conceitos e Técnicas Aplicadas
* **Conjuntos (`set`)**: Estrutura eficiente com tabela hash interna, com tempo de busca e verificação de pertinência médio $O(1)$.
* **Operador de União (`|`)**: Agrupa todos os elementos distintos de múltiplos conjuntos sem duplicação (`loja1 | loja2 | loja3 | loja4`).
* **Operador de Interseção (`&`)**: Isola apenas os elementos presentes em todos os conjuntos comparados simultaneamente (`loja1 & loja2 & loja3 & loja4`).
* **Operador de Diferença (`-`)**: 
  * `presentes - ao_menos_uma`: Identifica os presentes que nenhuma loja oferece.
  * `loja1 - (loja2 | loja3 | loja4)`: Identifica os produtos exclusivos da Loja 1 que nenhuma outra possui.
* **Otimização Combinatória**: Avaliação da cardinalidade `len(loja_a | loja_b)` para todos os 6 pares possíveis de lojas e seleção da melhor cobertura com `max()`.

---

## Processo de Construção

O desenvolvimento da solução no arquivo [`oficina.py`](./oficina.py) foi estruturado em 5 etapas:

1. **Definição dos Conjuntos:** Declaração do conjunto `presentes` com os 12 itens desejados e dos conjuntos `loja1`, `loja2`, `loja3` e `loja4` com seus respectivos catálogos.
2. **Cálculo da União Geral e Interseção:**
   * União das quatro lojas (`ao_menos_uma = loja1 | loja2 | loja3 | loja4`) para responder ao item 1;
   * Interseção quádrupla (`todas_as_lojas = loja1 & loja2 & loja3 & loja4`) para o item 2.
3. **Cálculo dos Presentes Ausentes:** Subtração dos itens disponíveis da lista total de presentes (`nenhuma_loja = presentes - ao_menos_uma`) para o item 3.
4. **Isolamento de Itens Exclusivos por Loja:** Para cada loja, subtração da união das outras três lojas, agrupando os resultados em uma lista iterável e exibindo cada loja com seu respectivo produto único.
5. **Avaliação de Cobertura de Pares de Lojas:** Cálculo da união de cada combinação de 2 lojas $\binom{4}{2} = 6$ pares, cálculo de seus comprimentos com `len()` e determinação da quantidade máxima coberta via `max()`.

---

## Resultados Obtidos

Ao executar o script `oficina.py`, o terminal apresenta o diagnóstico completo das compras:

```text
--- Planejamento de Presentes de Casamento ---
Total de presentes desejados: 12
Conjunto de presentes: {'Faqueiro', 'Aspirador de Pó', 'Jogo de Panelas', 'Jogo de Cama', 'Torradeira', 'Air Fryer', 'Batedeira', 'Ferro de Passar', 'Jogo de Toalhas', 'Micro-ondas', 'Liquidificador', 'Cafeteira'}

1. Produtos oferecidos em ao menos uma loja:
{'Faqueiro', 'Aspirador de Pó', 'Jogo de Panelas', 'Torradeira', 'Air Fryer', 'Batedeira', 'Jogo de Toalhas', 'Micro-ondas', 'Liquidificador', 'Cafeteira'}

2. Produtos oferecidos em todas as lojas:
{'Micro-ondas', 'Cafeteira'}

3. Produtos não encontrados em nenhuma loja:
{'Ferro de Passar', 'Jogo de Cama'}

4. Produtos exclusivos de cada loja:
- Loja 1: {'Faqueiro'}
- Loja 2: {'Batedeira'}
- Loja 3: {'Aspirador de Pó'}
- Loja 4: {'Air Fryer'}

5. Maior quantidade de presentes cobertos escolhendo duas lojas:
8 presentes

Pressione Enter para encerrar...
```

**Análise dos Resultados:**
* **Ao menos uma loja:** 10 dos 12 presentes pesquisados estão disponíveis no mercado.
* **Presentes universais:** Apenas **Cafeteira** e **Micro-ondas** são vendidos por todas as 4 lojas.
* **Produtos em falta:** Nem a Loja 1, 2, 3 ou 4 oferecem **Ferro de Passar** e **Jogo de Cama** (o casal precisará procurar em outra loja).
* **Exclusividade equilibrada:** Cada loja possui exatamente um produto exclusivo (Loja 1: Faqueiro, Loja 2: Batedeira, Loja 3: Aspirador de Pó, Loja 4: Air Fryer).
* **Melhor estratégia de compra:** Combinando 2 lojas (por exemplo, Loja 1 e Loja 2), o casal consegue comprar até **8 presentes diferentes**, maximizando a eficiência de compra.

---

## Arquivos da Aula
* [`oficina.py`](./oficina.py): Código Python com todas as operações de conjuntos e análise combinatória.

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
python "Aula 2.4 - Conjuntos e suas utilizações\oficina.py"
```
*(ou navegue até a pasta da aula e execute `python oficina.py`)*
