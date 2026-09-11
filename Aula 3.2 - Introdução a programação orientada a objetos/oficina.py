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
