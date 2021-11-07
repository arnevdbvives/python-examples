import gameobjects.ocean as ocean

class Player():

    def __init__(self, name):
        self.name = name
        self.__ocean = ocean.Ocean()
        self.__number_of_bombs = 10
        self.__number_of_bombs_left = 10

    def has_lost(self):
        if not self.__ocean.get_ship().is_sunk() and self.__number_of_bombs_left == 0:
            return True
        else:
            return False

    def has_won(self):
        return self.__ocean.get_ship().is_sunk()

    def drop_bomb(self,position):
        """Position is a tuple with the position in the sea
            We return 0 is the bomb is succesfully dropped with a hit,
            we return 1 is if it is in bounds but no hit
            -1 if it is out of bounds
        """
        bomb = self.__ocean.drop_bomb(position)
        if bomb == 0 or bomb == 1:
            self.__number_of_bombs_left -= 1
            return bomb
        else:
            return -1

    def get_ocean_grid(self):
        return self.__ocean.get_grid()

    def get_number_of_bombs_left(self):
        return self.__number_of_bombs_left


if __name__ == "__main__":
    john = Player("John")
    ocean = john.get_ocean_grid()
    length = len(ocean)
    for i in range(length):
        for j in range(length):
            print(ocean[i][j], end=" ")
        print(" ")




