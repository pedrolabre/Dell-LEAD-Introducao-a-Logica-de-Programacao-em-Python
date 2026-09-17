# Aula 3.2 - Introdução a programação orientada a objetos

Este módulo introduz o paradigma de **Programação Orientada a Objetos (POO)** em Python, abordando a modelagem e abstração de entidades do mundo real através de classes, instanciação de objetos, métodos construtores (`__init__`), atributos de instância, métodos especiais (*dunder methods*) como `__str__`, métodos de manipulação de estado, além de mecanismos para lançamento (`raise`) e tratamento de exceções com blocos `try / except` integrados a um menu iterativo em console.

---

## Objetivo da Aula
* Compreender os pilares da Programação Orientada a Objetos: abstração, classes, objetos, atributos e métodos;
* Declarar classes utilizando a palavra-reservada `class`;
* Implementar o método construtor `__init__` para inicialização segura dos atributos do objeto;
* Sobrescrever o método especial `__str__` para representação textual amigável do estado interno do objeto;
* Desenvolver métodos de instância para simular comportamentos e alterar o estado do objeto (`andar` e `comer`);
* Lançar exceções programáticas com `raise Exception` para validação de regras de negócio;
* Tratar exceções em tempo de execução com `try` e `except` (`ValueError`, `Exception`), impedindo travamentos abruptos do programa;
* Integrar o objeto a um menu de opções em console baseado em laço `while`.

---

## Enunciado da Oficina
> **Oficina Microlearning 12**
> 
> Os jogos de simulação são muito famosos e divertidos. Em SimCity, por exemplo, o jogador brinca de gerenciar uma cidade. Já em Tamagoshi, o jogador tem um pequeno dispositivo que simula toda a vida de um animal de estimação. Tendo como referência esses passatempos, que tal fazer uma pequena simulação como se você estivesse construindo uma pequena cópia do Tamagoshi?
> 
> Para esta oficina, a partir do que foi aprendido até aqui, você deverá construir uma classe para abstrair um animal qualquer. Nessa abstração, inclua os atributos `nome`, `espécie` e `fome`. Por exemplo, nome e espécie podem ser passados como parâmetro no construtor dessa classe; já a fome deve ser inicializada com valor 0, pois ela é o atributo indicador numérico que armazenará o quanto de fome o animal tem em um dado momento. Assim, 0 (zero) fome significa que ele está satisfeito, ou seja, não tem fome nenhuma. Agora, se tiver 1, significa que ele tem um pouquinho de fome; 2, um pouco mais; e assim por diante.
> 
> Como comportamento, você precisará construir o método `__str__()` para retornar uma string, representando o estado atual de um dado animal, e um método `andar()`, que simula um passeio com o animal. Ao andar, o valor da fome do animal deve aumentar em 1.
> 
> Além desses métodos, você deverá construir um método `comer()`, que implementa a simulação do ato do animal de se alimentar. Esse método recebe um valor numérico, como parâmetro, que é o número de unidades de comida oferecidas ao animal. Com esse valor, você vai diminuir o atributo fome do animal. Caso o valor de fome do animal seja menor do que o valor de comida oferecido, você deve atualizar o valor de fome para 0 (o valor mínimo possível) e informar ao usuário que o animal comeu até ficar saciado e deixou o resto da comida no prato.
> 
> Por fim, fora da classe, instancie um objeto `Animal` com o nome e espécie que você quiser. Feito isso, será possível criar um laço de repetição para interagir com o usuário. Ademais, deve haver um menu com 4 opções:
> 1. Alimentar o animal;
> 2. Andar com o animal;
> 3. Mostrar o estado atual do animal;
> 4. Finalizar execução.
> 
> O usuário vai digitar a opção que quer, e você vai fazer com que o animal se comporte adequadamente. Na opção 1, você vai apresentar uma nova questão ao usuário para que ele informe o quanto de comida é desejada para dar ao animal. Assim, você vai tratar a possível exceção gerada, informando ao usuário que ele deu comida demais, caso seja a situação. Ao final de cada interação, você vai apresentar o novo estado do animal e, depois, apresentar o menu novamente ao usuário até que ele escolha finalizar a execução do programa.
> 
> Empolgado para desenvolver esse joguinho? Então comece a praticar agora!

---

## Conceitos e Técnicas Aplicadas
* **Abstração e Encapsulamento (`class Animal`)**: Representação coesa das características e comportamentos do animal de estimação.
* **Construtor `__init__` e Referência `self`**: Instanciação da identidade de cada animal criado, vinculando seus dados específicos ao contexto do objeto.
* **Método Especial `__str__`**: Permite a impressão direta do objeto em chamadas `print(meu_animal)`, retornando uma representação legível e padronizada.
* **Regras de Negócio e Lançamento de Exceções (`raise Exception`)**:
  * Impede operações inconsistentes (como fornecer quantidade negativa de alimento);
  * Comunica ao chamador que o animal comeu além da necessidade sem quebrar a coerência do estado interno.
* **Tratamento de Exceções (`try / except`)**:
  * Captura de `ValueError` quando o usuário digita texto no lugar de um número inteiro;
  * Captura genérica de `Exception` para exibir de forma elegante as mensagens lançadas pelo método `comer()`.
* **Menu Interativo com Máquina de Estados**: Laço `while opcao != "4"` gerenciando o fluxo contínuo da aplicação.

---

## Processo de Construção

O desenvolvimento da solução no arquivo [`oficina.py`](./oficina.py) foi estruturado nas seguintes etapas:

1. **Modelagem da Classe `Animal`:**
   * Declaração de `__init__` recebendo `nome` e `especie`, inicializando `self.fome = 0`;
   * Declaração de `__str__` formatando `"Animal: {} | Espécie: {} | Nível de fome: {}"`;
   * Declaração de `andar()` incrementando `self.fome += 1`;
   * Declaração de `comer(comida)` com validação condicional e disparos de exceção controlados.
2. **Instanciação do Objeto Inicial:** Criação da instância `meu_animal = Animal("Totó", "Cachorro")`.
3. **Loop Principal da Interface de Console:**
   * Apresentação das opções numéricas de 1 a 4;
   * Roteamento de comandos via estruturas `if / elif / else`;
   * Execução das ações do objeto e exibição imediata do novo estado no terminal.

---

## Resultados Obtidos

Ao executar o script `oficina.py` e interagir com o menu do console, o terminal apresenta a seguinte simulação:

```text
=========================================
    BEM-VINDO AO SIMULADOR TAMAGOSHI    
=========================================
Seu animal foi criado com sucesso!
Animal: Totó | Espécie: Cachorro | Nível de fome: 0

--- MENU DE OPÇÕES ---
1 - Alimentar o animal
2 - Andar com o animal
3 - Mostrar estado atual do animal
4 - Finalizar execução
Digite a opção desejada (1-4): 2
Você passeou com o animal! A caminhada abriu o apetite dele.

Novo estado do animal:
Animal: Totó | Espécie: Cachorro | Nível de fome: 1

--- MENU DE OPÇÕES ---
1 - Alimentar o animal
2 - Andar com o animal
3 - Mostrar estado atual do animal
4 - Finalizar execução
Digite a opção desejada (1-4): 1
Informe o quanto de comida deseja dar ao animal: 2
Você deu comida demais! O animal comeu até ficar saciado e deixou o resto da comida no prato.

Novo estado do animal:
Animal: Totó | Espécie: Cachorro | Nível de fome: 0

--- MENU DE OPÇÕES ---
1 - Alimentar o animal
2 - Andar com o animal
3 - Mostrar estado atual do animal
4 - Finalizar execução
Digite a opção desejada (1-4): 3

Estado atual do animal:
Animal: Totó | Espécie: Cachorro | Nível de fome: 0

--- MENU DE OPÇÕES ---
1 - Alimentar o animal
2 - Andar com o animal
3 - Mostrar estado atual do animal
4 - Finalizar execução
Digite a opção desejada (1-4): 4

Encerrando o simulador Tamagoshi. Até a próxima!

Pressione Enter para encerrar...
```

**Análise dos Resultados:**
* A caminhada aumentou o nível de fome de `0` para `1`.
* Ao tentar alimentar com `2` unidades (maior que a fome de `1`), o método `comer` acionou a exceção com sucesso, zerando a fome sem permitir valores negativos e notificando o usuário amigavelmente.
* A navegação pelo menu respondeu de maneira contínua e robusta sem interrupções indesejadas.

---

## Arquivos da Aula
* [`oficina.py`](./oficina.py): Código Python com a classe `Animal`, métodos de ciclo de vida e menu interativo em console.

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
python "Aula 3.2 - Introdução a programação orientada a objetos\oficina.py"
```
*(ou navegue até a pasta da aula e execute `python oficina.py`)*
