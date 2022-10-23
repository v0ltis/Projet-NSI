from pokedex.pokemons import liste_pokemons
from functions.menu import show_pokemons, show_options, show_elements
from random import randint
from time import sleep
from beautifultable import BeautifulTable


def init_game() -> tuple:
    """
    Will show this little funny introduction to the game, and return the name of the IA & Player.

    return tuple[str, str]
    """
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


def show_menu() -> None:
    """
    Invoked after init_game() function being invoked

    Nothing is returned. This function is only executing other functions.
    """

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


def select_pokemon(ia_name) -> tuple:
    """
    Allow player to select its pokémons.

    Repeated three times:
        Player select its pokémon
        IA select a random unselected pokémon, regardless of its or the player's pokemons.

    then, user's and IA's pokemons are returned

    return Tuple[Tuple[Pokemon, Pokemon, Pokemon], Tuple[Pokemon, Pokemon, Pokemon]]
    """

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
        print(f"{ia_name} a sélectionnée {choix.nom}, de type {choix.element.name}.\n")

        sleep(1)

    return choix_user, choix_ia


def tour(joueur, ia, show_pokemons=True):

    """
    This function is called for each user's turn.

    It will show the pokemons of the user and the IA, and ask the user to pick an option (change pokemon, attack, give up or use special attack if possible).

    Joueur and IA are both of type Trainer

    show_pokemons is a boolean, if True, it will show the pokemons of the user and the IA.

    return "break" if the user wants to give up, a Pokemon Object if the player killed the IA's pokemon, False if the player killed the last pokemon of the IA,
        or return None if none of the above.
    """

    if show_pokemons:
        # Display trainers/pokémons infos
        table = BeautifulTable()
        table.set_style(BeautifulTable.STYLE_SEPARATED)
        table.columns.header = ["Joueur", "Pokemon", "Type", "PV", "Degats", "Pokémons en vie", "Attq Spé Dispo"]

        pokemon = joueur.pokemons[0]

        table.rows.append([joueur.name, pokemon.nom, pokemon.element.name, pokemon.pv, pokemon.ptdegat, joueur.alive_pokemons(), f"Oui ({pokemon.attaque_spe}pts)" if pokemon.attaque_spe_used == False else "Non"])

        pokemon = ia.pokemons[0]

        table.rows.append([ia.name, pokemon.nom, pokemon.element.name, pokemon.pv, pokemon.ptdegat, ia.alive_pokemons(), f"Oui ({pokemon.attaque_spe}pts)" if pokemon.attaque_spe_used == False else "Non"])

        print(table)

        print("\n\n")

    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_SEPARATED)
    table.columns.header = ["ID", "Description"]

    table.rows.append([0, "Changer de Pokemon"])

    table.rows.append([1, "Attaquer"])

    table.rows.append([2, "Quitter le Combat"])

    # case the user has a special attack available
    # will be showed in the table
    if joueur.pokemons[0].attaque_spe_used == False:
        table.rows.append([3, "Attaque spéciale"])

    print(table)

    # initialisation of response variable
    response = -1

    # If the user didn't used its special attack:
    # while his repsponse is not between 0 and 3
    # or if he used its special attack:
    # while his repsponse is not between 0 and 2
    #     ask the action ID
    while not ((0 <= response <= 3 and joueur.pokemons[0].attaque_spe_used == False) or 0 <= response <= 2):
        response = int(input("ID de l'action: "))

    # case the user give up
    if response == 2:
        return "break"

    # case the user want to change pokemon
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

    # case the user want to use a special attack AND can use it
    elif response == 3:
        poke_attaq = joueur.pokemons[0]

        pke_def = ia.pokemons[0]

        joueur.pokemons[0].attaque_spe_used = True

        is_dead, degats = poke_attaq.attaque_speciale(pke_def)

        if is_dead:
            print(f"\n{pke_def.nom} a été tué par {poke_attaq.nom} grâce à son attaque spéciale qui lui a infligé {degats} !\n")

            new_poke = ia.change_pokemon()

            if new_poke != False:
                print(f"\n{ia.name} a invoqué {new_poke.nom}, de type {new_poke.element.name} avec {new_poke.pv} PV\n")

            return new_poke

        else:
            print(f"\n{pke_def.nom} a été blessé par {poke_attaq.nom} grâce à son attaque spéciale qui lui a infligé {degats}pts !\n")

            return None

    # case the user want to attack
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
    """
    function dedicated to the ia combat turn.

    user represent the player Trainer object
    ia represent the IA Trainer object

    Return new_poke if the pokemon is dead, representing the new pokemon. If all pokemons are dead, return False. Else, return None
    """
    poke_attaq = ia.pokemons[0]

    pke_defence = user.pokemons[0]

    # randomly use special attaque if not used yet:
    # 1/3 chance
    if poke_attaq.attaque_spe_used == False and randint(1, 3) == 1:
        poke_attaq.attaque_spe_used = True

        is_dead, degats = poke_attaq.attaque_speciale(pke_defence)

        spe_att = True

    else:
        is_dead, degats = poke_attaq.attaque(pke_defence)

        spe_att = False

    # if the pokemon has been killed by the attack
    if is_dead:
        print(f"\n{poke_attaq.nom} a infligé {degats}pts de dégats et éliminé {pke_defence.nom} {'grace à son attaque spéciale ' if spe_att else ''}!")

        new_poke = user.change_pokemon()

        # if another pokemon is alive
        if new_poke != False:
                print(f"Vous avez invoqué {new_poke.nom}, de type {new_poke.element.name} avec {new_poke.pv} PV\n")

        return new_poke

    else:
        print(f"\n{poke_attaq.nom} a infligé {degats}pts de dégats à {pke_defence.nom} {'grace à son attaque spéciale ' if spe_att else ''}!\n")

        return None
