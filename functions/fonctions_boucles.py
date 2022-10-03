from pokedex.pokemons import liste_pokemons
from functions.menu import show_pokemons
from random import randint


def select_pokemon():

    choix_user = []

    choix_ia = []

    for i in range(3):
        id_pokemon = -1

        # CHOIX UTILISATEUR
        while not (0 <= id_pokemon < len(liste_pokemons)):

            print(show_pokemons(liste_pokemons))
            id_pokemon = int(input("ID du pokémon que vous souhaitez selectionner:"))

            if not 0 <= id_pokemon < len(liste_pokemons):
                print(f"/!\\ ERREUR: L'id du pokemon doit être compris entre 0 et {len(liste_pokemons)-1} /!\\\n")

        choix = liste_pokemons.pop(id_pokemon)

        choix_user.append(choix)

        print(f"Vous avez séléctionné {choix.nom}, de type {choix.element.name}.\n")

        # CHOIX IA
        choix = liste_pokemons.pop(
            randint(
                0, len(liste_pokemons)
            )
        )

        choix_ia.append(choix)
        print(f"l'IA a sélectionnée {choix.nom}, de type {choix.element.name}.\n\n\n")

    return choix_user, choix_ia

