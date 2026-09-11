# Classe de abstração do animal de estimação virtual


class Animal:
    """Classe que abstrai um animal de estimação virtual (Tamagoshi)."""

    def __init__(self, nome, especie):
        """Inicializa uma nova instância de Animal com nome, espécie e fome zerada."""
        self.nome = nome
        self.especie = especie
        self.fome = 0

    def __str__(self):
        """Retorna uma string representando o estado atual do animal."""
        return "Animal: {} | Espécie: {} | Nível de fome: {}".format(
            self.nome, self.especie, self.fome
        )

    def andar(self):
        """Simula um passeio com o animal, aumentando seu nível de fome em 1."""
        self.fome += 1

    def comer(self, comida):
        """Simula o ato de alimentar o animal.

        Recebe a quantidade de comida oferecida. Diminui o nível de fome.
        Caso a comida oferecida seja maior que a fome atual, zera a fome e
        lança uma exceção informando que o animal se saciou e sobrou comida.
        """
        if comida < 0:
            raise Exception("A quantidade de comida não pode ser negativa.")
        if comida > self.fome:
            self.fome = 0
            raise Exception(
                "Você deu comida demais! O animal comeu até ficar saciado e deixou o resto da comida no prato."
            )
        self.fome -= comida


# Programa principal / Simulação Tamagoshi

# Instanciação do objeto Animal
meu_animal = Animal("Totó", "Cachorro")

print("=========================================")
print("    BEM-VINDO AO SIMULADOR TAMAGOSHI    ")
print("=========================================")
print("Seu animal foi criado com sucesso!")
print(meu_animal)

# Laço de repetição com menu interativo
opcao = ""
while opcao != "4":
    print("\n--- MENU DE OPÇÕES ---")
    print("1 - Alimentar o animal")
    print("2 - Andar com o animal")
    print("3 - Mostrar estado atual do animal")
    print("4 - Finalizar execução")

    opcao = input("Digite a opção desejada (1-4): ")

    if opcao == "1":
        try:
            comida = int(input("Informe o quanto de comida deseja dar ao animal: "))
            meu_animal.comer(comida)
            print("O animal se alimentou com sucesso!")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")
        except Exception as erro:
            print(erro)
        print("\nNovo estado do animal:")
        print(meu_animal)

    elif opcao == "2":
        meu_animal.andar()
        print("Você passeou com o animal! A caminhada abriu o apetite dele.")
        print("\nNovo estado do animal:")
        print(meu_animal)

    elif opcao == "3":
        print("\nEstado atual do animal:")
        print(meu_animal)

    elif opcao == "4":
        print("\nEncerrando o simulador Tamagoshi. Até a próxima!")

    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")

input("\nPressione Enter para encerrar...")
