from pokedex.pokemons import liste_pokemons
from functions.menu import show_pokemons, show_options, show_elements
from random import randint
from time import sleep


def init_game() -> tuple[str, str]:
    print("Professeur Chen: Bonjour euh ... jeune dresseur !")
    sleep(1.25)
    name = input("Professeur Chen: Comment t'appelles tu déjà ?\nVous: ")
    sleep(0.5)
    print(f"Professeur Chen: Mais bien sûr, {name} ... je n'avais pas oublié ... pas du tout ...")
    sleep(2.5)
    print(f"Professeur Chen: Aujourd'hui j'ai une bonne nouvelle à t'annoncer, tu va te battre contre euuh ...")
    sleep(2.5)
    ai_name = input("Professeur Chen: Tu pourrais me rappeler le nom de ton adversaire ?\nVous: ")
    sleep(0.25)
    print(f"Professeur Chen: Oui voilà, {ai_name}, je l'avais sur le bout de la langue !")
    sleep(2.5)
    print(
        f"Professeur Chen: Bien {name}, tu va pouvoir séléctionner tes Pokémon. Tu peux également regarder les forces et faiblesses des types, ...")
    sleep(2.5)
    print("Professeur Chen: À bientôt, et bon combat !\n\n")
    sleep(2.5)

    return name, ai_name


def show_menu():
    menu_keys = [
        show_pokemons,
        show_elements,
        select_pokemon
    ]

    first_boucle = True

    while True:

        if not first_boucle:
            sleep(2)
            print("\n\n\n")

        first_boucle = False

        print(show_options())

        id_menu = int(input("ID du menu que vous souhaitez voir:"))

        if id_menu >= len(menu_keys):
            print(f"/!\\ ERREUR: L'id du menu doit être compris entre 0 et {len(menu_keys) - 1} /!\\\n")

        elif id_menu == 2:
            break

        else:
            print("\n",
                  menu_keys[id_menu](),
                  "\n"
                  )


def select_pokemon():
    choix_user = []

    choix_ia = []

    for i in range(3):
        id_pokemon = -1

        # CHOIX UTILISATEUR
        while not (0 <= id_pokemon < len(liste_pokemons)):

            print(show_pokemons(liste_pokemons))
            id_pokemon = int(input("ID du pokémon que vous souhaitez sélectionner:"))

            if not 0 <= id_pokemon < len(liste_pokemons):
                print(f"/!\\ ERREUR: L'id du pokemon doit être compris entre 0 et {len(liste_pokemons) - 1} /!\\\n")

        choix = liste_pokemons.pop(id_pokemon)

        choix_user.append(choix)

        print(f"Vous avez sélectionné {choix.nom}, de type {choix.element.name}.\n")

        sleep(0.5)

        # CHOIX IA
        choix = liste_pokemons.pop(
            randint(
                0, len(liste_pokemons) - 1
            )
        )

        choix_ia.append(choix)
        print(f"l'IA a sélectionnée {choix.nom}, de type {choix.element.name}.\n")

        sleep(1)

    return choix_user, choix_ia
