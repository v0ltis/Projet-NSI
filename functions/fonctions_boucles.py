from pokedex.pokemons import liste_pokemons
from functions.menu import show_pokemons, show_options, show_elements
from random import randint
from time import sleep
from beautifultable import BeautifulTable


def init_game():
    print("Professeur Chen: Bonjour euh ... jeune dresseur !")
    sleep(1.25)
    name = input("Professeur Chen: Comment t'appelles tu déjà ?\nVous: ")
    sleep(0.5)
    print(f"Professeur Chen: Mais bien sûr, {name} ... je n'avais pas oublié ... pas du tout ...")
    sleep(2.5)
    print(f"Professeur Chen: Aujourd'hui j'ai une bonne nouvelle à t'annoncer, tu vas te battre contre euuh ...")
    sleep(2.5)
    ai_name = input("Professeur Chen: Tu pourrais me rappeler le nom de ton adversaire ?\nVous: ")
    sleep(0.25)
    print(f"Professeur Chen: Oui voilà, {ai_name}, je l'avais sur le bout de la langue !")
    sleep(2.5)
    print(f"Professeur Chen: Bien {name}, tu vas pouvoir séléctionner tes pokémons. Tu peux également regarder les forces et faiblesses des types, ...")
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


def tour(joueur, ia, show_pokemons=True):
    if show_pokemons:
        table = BeautifulTable()
        table.set_style(BeautifulTable.STYLE_SEPARATED)
        table.columns.header = ["Joueur", "Pokemon", "Element", "pv", "degats", "Pokémons en vie"]

        pokemon = joueur.pokemons[0]

        table.rows.append([joueur.name, pokemon.nom, pokemon.element.name, pokemon.pv, pokemon.ptdegat, joueur.alive_pokemons()])

        pokemon = ia.pokemons[0]

        table.rows.append([ia.name, pokemon.nom, pokemon.element.name, pokemon.pv, pokemon.ptdegat, ia.alive_pokemons()])

        print(table)

        print("\n\n")

    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_SEPARATED)
    table.columns.header = ["ID", "Description"]

    table.rows.append([0, "Changer de Pokemon"])

    table.rows.append([1, "Attaquer"])

    table.rows.append([2, "Quitter le Combat"])

    print(table)

    response = -1

    while not (0 <= response <= 2):
        response = int(input("ID de l'action: "))

    if response == 2:
        return "break"

    elif response == 0:
        poke1 = joueur.pokemons[1]
        poke2 = joueur.pokemons[2]

        if poke1.dead == poke2.dead == True:
            print("\n\nVos pokémons sont morts")

            return tour(joueur, ia, show_pokemons=False)

        else:
            new_poke = joueur.change_pokemon()

            if new_poke != False:
                print(f"\nVous avez invoqué {new_poke.nom}, de type {new_poke.element.name} avec {new_poke.pv} PV\n")

            return tour(joueur, ia, show_pokemons=False)

    else:
        poke_attaq = joueur.pokemons[0]

        pke_defence = ia.pokemons[0]

        is_dead, degats = poke_attaq.attaque(pke_defence)

        if is_dead:
            print(f"\n{poke_attaq.nom} a infligé {degats}pts de dégats et éliminé {pke_defence.nom} !")

            new_poke = ia.change_pokemon()

            if new_poke != False:
                print(f"{ia.name} a invoqué {new_poke.nom}, de type {new_poke.element.name} avec {new_poke.pv} PV\n")

            return new_poke

        else:
            print(f"\n{poke_attaq.nom} a infligé {degats}pts de dégats à {pke_defence.nom} !\n")

            return None


def tour_ia(user, ia):
    poke_attaq = ia.pokemons[0]

    pke_defence = user.pokemons[0]

    is_dead, degats = poke_attaq.attaque(pke_defence)

    if is_dead:
        print(f"\n{poke_attaq.nom} a infligé {degats}pts de dégats et éliminé {pke_defence.nom} !")

        new_poke = user.change_pokemon()

        if new_poke != False:
            print(f"Vous avez invoqué {new_poke.nom}, de type {new_poke.element.name} avec {new_poke.pv} PV\n")

        return new_poke

    else:
        print(f"\n{poke_attaq.nom} a infligé {degats}pts de dégats à {pke_defence.nom} !\n")

        return None
