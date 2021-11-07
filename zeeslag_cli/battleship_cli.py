import gameobjects.player as player


def print_ocean(ocean):
    length = len(ocean)
    print(" ", end="  ")
    for i in range(length):
        print(str(i), end="  ")
    print(" ")
    for i in range(length):
        print(str(i), end="  ")
        for j in range(length):
            print(ocean[i][j], end="  ")
        print(" ")


if __name__ == '__main__':
    print("Welcome to battleship!")
    name = input("Give me your name: ")
    player = player.Player(name)
    print("You have to bomb a ship of 3 position long in a square see of 5 to 5.")
    while not player.has_won() and not player.has_lost():
        print(f"{player.name}, you have {player.get_number_of_bombs_left()} of bombs left. "
              f"Where do want to throw you next bomb")
        row = int(input("What the row number of your next bomb? "))
        column = int(input("What the column number of your next bomb? "))
        bomb = player.drop_bomb((row,column))
        if bomb == -1:
            print("Your bomb is not in the ocean.")
        elif bomb == 0:
            print("Congratulations! You hit the ship")
        else:
            print("I'm sorry. You missed the ship.")
        print_ocean(player.get_ocean_grid())
    if player.has_won():
        print(f"Congrulations {player.name}! You won. You sank the ship.")
    if player.has_lost():
        print("{player.name}, you have no bombs left and the ship is still sailing. You lost.")
