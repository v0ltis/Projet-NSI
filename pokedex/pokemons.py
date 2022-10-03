# louis lebert

from pokedex.elements import *


class Pokemon:
    def __init__(self, nom: str, element, pv: int, ptdegat: int):
        """
        element: correspond a une classe se trouvant dans element.py
        self.dead: correspond si le pokemon est mort ou pas
        """
        self.nom = nom
        self.element = element
        self.pv = pv
        self.ptdegat = ptdegat
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
        if pokemon_ennemi.element in self.element.weakness:
            pokemon_ennemi.pv -= self.ptdegat * 0.5

        elif pokemon_ennemi.element in self.element.strength:
            pokemon_ennemi.pv -= self.ptdegat * 2

        else:
            pokemon_ennemi.pv -= self.ptdegat * 1

        return pokemon_ennemi.verif_mort()


liste_pokemons = [
    Pokemon("Magicarpe", Water(), 100, 249),
    Pokemon("Phyllali", Grass(), 100, 50),
    Pokemon("Pharamp", Elec(), 100, 50),
    Pokemon("Wailord", Water(), 100, 50),
    Pokemon("Elekable", Grass(), 100, 50),
    Pokemon("Sorbouboule", Ice(), 100, 50),
    Pokemon("Polagriffe", Ice(), 100, 50),
    Pokemon("Gamblaste", Grass(), 100, 50),
    Pokemon("Zeraora", Elec(), 100, 50),
    Pokemon("Arcanin", Fire(), 100, 50),
    Pokemon("Pyrobut", Fire(), 100, 50)
]
