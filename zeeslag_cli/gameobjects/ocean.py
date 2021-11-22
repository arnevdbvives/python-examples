from typing import List, Tuple
from random import randint, choice
import gameobjects.ship as ship

class Ocean:

    def __init__(self, dimension=5):
        self.__dimension = dimension
        self.__grid = [["." for column in range(dimension)] for row in range(dimension)]
        self.__ship = choice([self.__position_ship_horizontal(3),self.__position_ship_vertical(3)])

    def __position_ship_vertical(self, size: int) -> ship.Ship:
        """
        Chooses a random position of the ship in the ocean when we position the ship vertically
        size: size of the ship
        return: Ship
        """
        row = randint(0, self.__dimension - size)
        column = randint(0, self.__dimension - 1)
        positions = []
        for i in range(size):
            positions.append((row + i, column))
        return ship.Ship(positions)

    def __position_ship_horizontal(self, size: int) -> ship.Ship:
        """
        Chooses a random position of the ship in the ocean when we position the ship horizontally
        size: size of the ship
        return: Ship
        """
        row = randint(0, self.__dimension - 1)
        column = randint(0, self.__dimension - size)
        positions = []
        for i in range(size):
            positions.append((row, column + i))
        return ship.Ship(positions)

    def get_ship(self) -> ship.Ship:
        return self.__ship

    def get_dimension(self) -> int:
        return self.__dimension

    def get_grid(self) -> List[List[str]]:
        return self.__grid.copy()

    def drop_bomb(self, position: Tuple) -> int:
        """position is a tuple with the positions
        we return 0 if position is in grid and there is a hit
        1 if there it is in grid but no hit
        -1 if it is out of bounds
        """
        if position[0] < self.__dimension and position[1] < self.__dimension:
            hit = self.__ship.throw_bomb(position)
            if hit == 0:
                self.__grid[position[0]][position[1]] = "X"
                return 0
            else:
                self.__grid[position[0]][position[1]] = "0"
                return 1
        else:
            return -1


if __name__ == "__main__":
    my_ocean = Ocean(5)
    print(my_ocean.get_dimension())
    print(my_ocean.drop_bomb((4,4)))