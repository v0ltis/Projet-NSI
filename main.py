from functions.fonctions_boucles import select_pokemon, init_game, show_menu
from pokedex.trainer import Trainer


def main():
    username, ia_name = init_game()

    show_menu()

    poke_user, poke_ia = select_pokemon()

    user = Trainer(username, poke_user)

    ia = Trainer(ia_name, poke_user)

    round = 1

    while True:

        if round == 1:
            print("C'est parti !")
            print("Le combat va commencer.")
            print(f"D'un coté, {user.name}, avec {user.pokemons[0].nom}, {user.pokemons[1].nom} et {user.pokemons[2].nom}")
            print(f"Et en face, {ia.name}, avec {ia.pokemons[0].nom}, {ia.pokemons[1].nom} et {ia.pokemons[2].nom}")

        round += 1

if __name__ == "__main__":
    main()
