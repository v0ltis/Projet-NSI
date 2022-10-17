# By Barnabe

class Trainer:
    def __init__(self, name: str, pokemons: list):

        self.name = name

        self.pokemons = pokemons

    def change_pokemon(self):
        """
        Change the selected Pokémon ("Rotate" the list to the next alive Pokémon, if any)

        :return: False or the new selected Pokémon at index 0
        """

        for i in range(3):

            # "rotate" the list pokemon
            # Ex: [1, 2, 3] will become [2, 3, 1], then [3, 1, 2], and finally [1, 2, 3] again.
            # It will allow to switch between pokémons
            self.pokemons = self.pokemons[1:] + self.pokemons[:1]

            if not self.pokemons[0].dead:
                # return the pokémons No. 0 if it is not dead
                return self.pokemons[0]

        # If all pokémons are dead, the loop will be completed without returning anything.
        # returning False will be considered as loosing.
        return False

    def alive_pokemons(self) -> int:
        """
        Return the number of alive pokemons
        """

        return len([
                pokemon for pokemon in self.pokemons if not pokemon.dead
        ])
