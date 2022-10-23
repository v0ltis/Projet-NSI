from functions.fonctions_boucles import select_pokemon, init_game, show_menu, tour, tour_ia
from pokedex.trainer import Trainer
import time


def main():
    
    #username = "joueur"
    #ia_name = "ia"

    username, ia_name = init_game()
    
    show_menu()

    poke_user, poke_ia = select_pokemon(ia_name)

    user = Trainer(username, poke_user)

    ia = Trainer(ia_name, poke_ia)

    round = 1

    while True:

        if round == 1:
            print("C'est parti !")
            time.sleep(1)
            print("Le combat va commencer.")
            time.sleep(1)
            print(f"D'un coté, {user.name}, avec {user.pokemons[0].nom}, {user.pokemons[1].nom} et {user.pokemons[2].nom}")
            time.sleep(1)
            print(f"Et en face, {ia.name}, avec {ia.pokemons[0].nom}, {ia.pokemons[1].nom} et {ia.pokemons[2].nom}")
            time.sleep(1)

        """
        The three lines below will show something like:
        
        / ==================== \
                 Tour 1
        \ ==================== /
        """
        print("\n\n/", "="*20, "\\")
        print(" " * 8, f"Tour {round}")
        print("\\", "=" * 20, "/\n\n")
        time.sleep(2)

        # result of the Player's turn
        result = tour(user, ia)

        # If Player abandoned the game
        if result == "break":
            winner = ia
            break

        # If all IA's pokémons are dead
        if result == False:
            winner = user
            break

        time.sleep(2.5)

        # result of the IA's turn
        result = tour_ia(user, ia)

        # If all users's pokémons are dead
        if result == False:
            winner = ia
            break
        
        round += 1

    # end of the boucle
    # Display the winner
    poke = f"avec {winner.alive_pokemons()} pokemon{'s' if winner.alive_pokemons() != 1 else ''}"

    if result == "break":

        print(f"{winner.name} a gagné la partie par abandon, {poke} !")

    else:
        print(f"{winner.name} a gagné la partie, {poke} !")


if __name__ == "__main__":
    main()
