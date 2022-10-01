# tools for generating printable tables
# https://pypi.org/project/beautifultable/
from beautifultable import BeautifulTable
from pokedex.elements import elements_list


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
            element.name.capitalize(),      # Element
            weakns,                         # Faiblaisses
            strght                          # Forces
        ])

    return table


def show_options() -> BeautifulTable:
    """
    Return an str ASCII table of the list of availlables actions.

    the ID of the action and the description will be displayed

    Return BeatifulTable object (can be printed without precautions)
    """

    x = {
        "1": "Afficher les pokemons",
        "2": "Afficher les types",
        "3": "Choisir vos Pokémons"
    }

    table = BeautifulTable()
    table.columns.header = ["ID", "Description"]

    table.set_style(BeautifulTable.STYLE_SEPARATED)

    # add items to the table
    for key, item in x.items():

        table.rows.append([key, item])

    return table
