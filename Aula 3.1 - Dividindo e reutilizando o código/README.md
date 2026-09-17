# Aula 3.1 - Dividindo e reutilizando o código

Este módulo aborda o princípio da modularização e reutilização de código através de **funções** em Python, explorando a definição de sub-rotinas com `def`, documentação técnica através de `docstrings` (PEP 257), desempacotamento de tuplas, passagem flexível de parâmetros posicionais e nomeados (*keyword arguments*), e definição de argumentos padrão (*default arguments*).

---

## Objetivo da Aula
* Compreender o conceito de funções, escopo de variáveis e retorno de valores em Python;
* Escrever funções puras e modulares com responsabilidade única;
* Documentar rotinas e contratos de funções utilizando `docstrings` estruturadas;
* Aplicar desempacotamento posicional de tuplas para datas e horários;
* Definir parâmetros com valores pré-estabelecidos (*default arguments*) para tornar chamadas de funções flexíveis e opcionais;
* Comparar e invocar funções utilizando tanto argumentos posicionais quanto argumentos nomeados.

---

## Enunciado da Oficina
> **Oficina Microlearning 11**
> 
> Chegou o momento de você colocar em prática o que pôde aprender sobre dividir e reutilizar códigos. Para isso, imagine um programa de agenda, que utiliza uma lista para armazenar os eventos inseridos por um usuário, em que uma de suas finalidades é imprimir uma lista dos eventos que acontecerão entre duas datas especificadas também pelo usuário. Os eventos são representados por tuplas, confira:
> 
> * O primeiro elemento é uma tupla de três números: ano, mês e dia;
> * O segundo elemento é uma tupla de dois números: hora e minuto;
> * O terceiro elemento é uma string que descreve brevemente o evento.
> 
> Um exemplo dos dados dessa agenda é representado pelo seguinte trecho:
> 
> ```python
> agenda = [
>     ((2020, 1, 13), (11, 50), 'Renovar identidade'),
>     ((2020, 1, 15), (16, 30), 'Fazer compras'),
>     ((2020, 1, 25), (8, 45), 'Autenticar documentos'),
>     ((2020, 2, 29), (14, 15), 'Prestar concurso'),
>     ((2020, 3, 15), (17, 50), 'Buscar bolo pro aniversário da vovó'),
>     ((2020, 3, 17), (13, 20), 'Consulta de revisão com dentista')
> ]
> ```
> 
> Você deve completar a função `imprimir_eventos`, rascunhada a seguir, que recebe como parâmetros uma lista de eventos neste formato e dois parâmetros adicionais, `de_data` e `ate_data`, que dão as datas inicial e final:
> 
> ```python
> def imprimir_eventos(eventos, de_data=(1, 1, 1), ate_data=(9999, 12, 31)):
> ```
> 
> Os valores padrão das datas indicam que o comportamento padrão é imprimir todos os eventos. É possível restringir a data inicial, a data final ou ambas, usando estes parâmetros. Por exemplo, o resultado da chamada `imprimir_eventos(agenda, (2020, 1, 20))` é a impressão do seguinte trecho:
> 
> ```text
> 25/jan/2020 - 08:45: Autenticar documentos
> 29/fev/2020 - 14:15: Prestar concurso
> 15/mar/2020 - 17:50: Buscar bolo pro aniversário da vovó
> 17/mar/2020 - 13:20: Consulta de revisão com dentista
> ```
> 
> E o resultado da chamada `imprimir_eventos(agenda, ate_data=(2020, 3, 15))` é a impressão de:
> 
> ```text
> 13/jan/2020 - 11:50: Renovar identidade
> 15/jan/2020 - 16:30: Fazer compras
> 25/jan/2020 - 08:45: Autenticar documentos
> 29/fev/2020 - 14:15: Prestar concurso
> 15/mar/2020 - 17:50: Buscar bolo pro aniversário da vovó
> ```
> 
> Para auxiliar você na conclusão desse problema, crie também duas funções adicionais:
> 
> * `formatar_data`, que recebe uma tupla de números na forma `(ano, mes, dia)` e retorna uma string na forma `dd/mes/aaaa`, substituindo o mês pelas três letras iniciais do nome do mês, por extenso. Por exemplo, `formatar_data((2020, 1, 3))` deve retornar `"03/jan/2020"`;
> * `formatar_hora`, que recebe uma tupla de números na forma `(hora, minuto)` e retorna uma string na forma `hh:mm` em formato de 24h. Por exemplo, `formatar_hora((16, 30))` deve retornar `"16:30"`.
> 
> Então, agora é o momento de unir todas essas informações ao que você já sabe sobre funções para completar o programa de acordo com as orientações passadas. Boa prática!

---

## Conceitos e Técnicas Aplicadas
* **Modularização com Funções (`def`)**: Divisão do problema em funções especializadas com baixo acoplamento (`formatar_data`, `formatar_hora`, `imprimir_eventos`).
* **Documentação Técnica (`docstrings`)**: Inclusão de blocos explicativos de três aspas logo abaixo da assinatura de cada função, esclarecendo parâmetros, tipos esperados e retornos.
* **Desempacotamento de Tuplas**:
  * `ano, mes, dia = data`: Extração dos elementos posicionais da tupla.
  * `hora, minuto = horario`: Extração simplificada de horas e minutos.
* **Mapeamento de Meses**: Tupla imutável com abreviações de meses indexada por `mes - 1`.
* **Argumentos Padrão (*Default Arguments*)**: `de_data=(1, 1, 1)` e `ate_data=(9999, 12, 31)` cobrem toda a linha do tempo se nenhum filtro for passado na chamada.
* **Comparação Direta de Tuplas**: No Python, tuplas numéricas do tipo `(ano, mes, dia)` suportam comparações relacionais naturais de ordem lexicográfica (`de_data <= data <= ate_data`), facilitando a filtragem cronológica sem necessidade de conversões adicionais.

---

## Processo de Construção

O desenvolvimento da solução no arquivo [`oficina.py`](./oficina.py) foi estruturado nas seguintes etapas:

1. **Implementação de `formatar_data`:** Extração de `ano`, `mes` e `dia`, consulta à tupla de meses por extenso e retorno com interpolação `{:02d}/{}/{:04d}`.
2. **Implementação de `formatar_hora`:** Extração de `hora` e `minuto` e formatação com dois dígitos `{:02d}:{:02d}`.
3. **Implementação de `imprimir_eventos`:**
   * Declaração dos parâmetros opcionais com valores de contorno mínimo e máximo;
   * Laço de iteração desempacotando `data, hora, descricao` da lista de eventos;
   * Teste condicional de intervalo `de_data <= data <= ate_data`;
   * Invocação das funções auxiliares de formatação e exibição da linha de log.
4. **Definição da Base de Testes e Validação:** Declaração da lista `agenda` e execução de 4 baterias de testes contemplando chamadas posicionais, nomeadas e default.

---

## Resultados Obtidos

Ao executar o script `oficina.py`, o terminal apresenta a saída de todos os cenários testados:

```text
--- Sistema de Gerenciamento de Eventos da Agenda ---

--- Eventos a partir de 20/01/2020 (data inicial posicional) ---
25/jan/2020 - 08:45: Autenticar documentos
29/fev/2020 - 14:15: Prestar concurso
15/mar/2020 - 17:50: Buscar bolo pro aniversário da vovó
17/mar/2020 - 13:20: Consulta de revisão com dentista

--- Eventos até 15/03/2020 (data final nomeada) ---
13/jan/2020 - 11:50: Renovar identidade
15/jan/2020 - 16:30: Fazer compras
25/jan/2020 - 08:45: Autenticar documentos
29/fev/2020 - 14:15: Prestar concurso
15/mar/2020 - 17:50: Buscar bolo pro aniversário da vovó

--- Todos os eventos cadastrados (parâmetros padrão) ---
13/jan/2020 - 11:50: Renovar identidade
15/jan/2020 - 16:30: Fazer compras
25/jan/2020 - 08:45: Autenticar documentos
29/fev/2020 - 14:15: Prestar concurso
15/mar/2020 - 17:50: Buscar bolo pro aniversário da vovó
17/mar/2020 - 13:20: Consulta de revisão com dentista

--- Eventos no intervalo entre 15/01/2020 e 29/02/2020 ---
15/jan/2020 - 16:30: Fazer compras
25/jan/2020 - 08:45: Autenticar documentos
29/fev/2020 - 14:15: Prestar concurso

Pressione Enter para encerrar...
```

**Análise dos Resultados:**
* A flexibilidade na passagem de argumentos permitiu reutilizar exatamente a mesma rotina de impressão em 4 contextos de filtragem distintos.
* A formatação de datas e horas padronizou a exibição com zeros à esquerda (ex.: `08:45`, `13/jan/2020`).
* A comparação relacional nativa entre tuplas comprovou-se matematicamente idêntica à comparação cronológica de datas.

---

## Arquivos da Aula
* [`oficina.py`](./oficina.py): Código Python com a declaração das funções de formatação, filtragem e cenários de teste.

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
python "Aula 3.1 - Dividindo e reutilizando o código\oficina.py"
```
*(ou navegue até a pasta da aula e execute `python oficina.py`)*
