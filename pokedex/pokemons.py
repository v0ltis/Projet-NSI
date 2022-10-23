# louis lebert

from pokedex.elements import *


class Pokemon:
    def __init__(self, nom: str, element, pv: int, ptdegat: int, attaque_spe:int):
        """
        element: correspond a une classe se trouvant dans element.py
        self.dead: correspond si le pokemon est mort ou pas
        """
        self.nom = nom
        self.element = element
        self.pv = pv
        self.ptdegat = ptdegat
        self.attaque_spe = attaque_spe
        self.attaque_spe_used = False
        self.dead = False

    def verif_mort(self):
        """
        verifie si le pokemon est mort ou pas
        """
        if self.pv <= 0:
            self.dead = True
            return True

        else:
            return False

    def attaque(self, pokemon_ennemi):
        """
        on regarde les faiblesses et les forces du type du pokemon
        si il est dans ces forces alors les degats sont multipliés par 2
        si il est dans ces faiblesses alors les degats sont multipliés par 0.5
        et si il est dans aucun des 2 alors les degats sont multipliés par 1
        return pokemon_ennemi.verif_mort(): on appelle notre fonction verif_mort
        pour regarder a chaque attaque si le pokemon est mort ou pas
        """

        damage = self.ptdegat

        if type(pokemon_ennemi.element) in self.element.weakness:
            damage //= 2

        elif type(pokemon_ennemi.element) in self.element.strength:
            damage *= 2

        pokemon_ennemi.pv -= damage

        return pokemon_ennemi.verif_mort(), damage

    def attaque_speciale(self, pokemon_ennemi):
        """
        on regarde les faiblesses et les forces du type du pokemon
        si il est dans ces forces alors les degats sont multipliés par 2
        si il est dans ces faiblesses alors les degats sont multipliés par 0.5
        et si il est dans aucun des 2 alors les degats sont multipliés par 1
        return pokemon_ennemi.verif_mort(): on appelle notre fonction verif_mort
        pour regarder a chaque attaque si le pokemon est mort ou pas
        """

        pokemon_ennemi.pv -= self.attaque_spe

        return pokemon_ennemi.verif_mort(), self.attaque_spe


liste_pokemons = [
    Pokemon("Magicarpe", Water(), 30, 200, 250),
    Pokemon("Phyllali", Grass(), 160, 100, 125),
    Pokemon("Pharamp", Elec(), 180, 80, 105),
    Pokemon("Wailord", Water(), 200, 70, 95),
    Pokemon("Elekable", Elec(), 190, 70, 95),
    Pokemon("Sorbouboule", Ice(), 200, 90, 115),
    Pokemon("Polagriffe", Ice(), 250, 80, 120),
    Pokemon("Gamblaste", Water(), 150, 90, 120),
    Pokemon("Zeraora", Elec(), 150, 110, 140),
    Pokemon("Arcanin", Fire(), 180, 80, 110),
    Pokemon("Maganon", Fire(), 190, 70, 95),
    Pokemon("Jungko", Grass(), 170, 90, 115),
    Pokemon("Ronflex", Normal(), 1500, 0, 5),
    Pokemon("Aspicot", Grass(), 15, 10, 12),
    Pokemon("Roucool", Normal(), 110, 60, 150),
    Pokemon("Tentacool", Water(), 120, 110, 125)
]
