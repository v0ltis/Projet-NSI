# tools for generating printable tables
# https://pypi.org/project/beautifultable/
from beautifultable import BeautifulTable
from pokedex.elements import elements_list
from pokedex.pokemons import liste_pokemons


def show_elements() -> BeautifulTable:
    """
    Return an str ASCII table of the list of elements in pokedex/elements.py.

    The name, weakness, and strenght will be printed in a board

    Return BeatifulTable object (can be printed without precautions)
    """

    # Generate the table
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_SEPARATED)
    table.columns.header = ["Element", "Faiblaisses", "Forces"]

    # Add all elements of ../pokedex/elements.py in the table.
    for i in range(len(elements_list)):
        element = elements_list[i]

        # Allow a pretty way to display a list in a string.
        weakns = ", ".join(
            i().name.capitalize() for i in element.weakness
        )

        strght = ", ".join(
            i().name.capitalize() for i in element.strength
        )

        # Add items to the table.
        table.rows.append([
            element.name.capitalize(),  # Element
            weakns,  # Faiblaisses
            strght  # Forces
        ])

    return table


def show_options() -> BeautifulTable:
    """
    Return a str ASCII table of the list of available actions.

    the ID of the action and the description will be displayed

    Return BeatifulTable object (can be printed without precautions)
    """

    menu_keys = [
        "Afficher les pokemons",
        "Afficher les types",
        "Choisir vos Pokémons"
    ]

    table = BeautifulTable()
    table.columns.header = ["ID", "Description"]

    table.set_style(BeautifulTable.STYLE_SEPARATED)

    # add items to the table
    for i in range(len(menu_keys)):
        table.rows.append([str(i), menu_keys[i]])

    return table


def show_pokemons(poke_list=liste_pokemons) -> BeautifulTable:
    """
    poke_list représente la liste des pokémons disponilbles à la selection

    Renvois une table en ASCII des pokemons disponibles.
    """
    table = BeautifulTable()
    table.columns.header = ["ID", "Nom", "Type", "PV", "Dégats", "Dégats Spé"]

    table.set_style(BeautifulTable.STYLE_RST)

    # add items to the table
    for i in range(len(poke_list)):
        pokemon = poke_list[i]

        table.rows.append([
            str(i),
            pokemon.nom,
            pokemon.element.name.capitalize(),
            pokemon.pv,
            pokemon.ptdegat,
            pokemon.attaque_spe
        ])

    return table
