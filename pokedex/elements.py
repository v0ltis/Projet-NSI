# By Barnabe
# Represent 6 pokémon element
#
# Name field is the displayed name
# weakness is a list of elements thant the pokémon deals x0.5 damages
# strength is a list of elements that the pokémon deals x2 damages


class Fire:
    def __init__(self):
        self.name = "feu"

        self.weakness = [
            Fire,
            Water
        ]

        self.strength = [
            Grass,
            Ice
        ]


class Water:
    def __init__(self):
        self.name = "eau"

        self.weakness = [
            Water,
            Grass
        ]

        self.strength = [
            Fire,
        ]


class Elec:
    def __init__(self):
        self.name = "éléctricité"
        
        self.weakness = [
            Elec,
            Grass
        ]
        
        self.strength = [
            Water
        ]


class Grass:
    def __init__(self):
        self.name = "plante"
        
        self.weakness = [
            Fire,
            Grass
        ]
        
        self.strength = [
            Water
        ]


class Ice:
    def __init__(self):
        self.name = "glace"
        
        self.weakness = [
            Fire,
            Water, 
            Ice
        ]
        
        self.strength = [
            Grass
        ]


# Usefull for functions/menu.py :
# Just need to use `for x in elements_list` instead of `for x in pokedex.elements` wich is unsafe
elements_list = [
    Fire(),
    Water(),
    Elec(),
    Grass(),
    Ice()
]
