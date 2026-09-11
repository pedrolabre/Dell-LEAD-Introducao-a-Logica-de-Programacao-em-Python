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
