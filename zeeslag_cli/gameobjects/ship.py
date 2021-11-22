from typing import List, Tuple  # needed to annotate positions as a list of tuples

class Ship():

    def __init__(self, positions: List[Tuple]):
        """
        positions: List[Tuple]  Positions is a row of tuples with the positions of the ship in the ocean.
        """
        self.__positions = positions
        self.__sunk = False
        self.__size = len(positions)
        self.__number_of_hits = 0
        self.__already_bombed = []
        for i in range(len(positions)):
            self.__already_bombed.append(False)

    def get_positions(self) -> List[Tuple]:
        return self.__positions

    def throw_bomb(self, position) -> int:
        """
        position is a tuple with a position in the grid
        return 0 is there is a hit, -1 if there is no hit
        """
        if position in self.__positions:
            index = self.__positions.index(position)
            if not self.__already_bombed[index]:
                self.__already_bombed[index] = True
                self.__number_of_hits += 1
            if self.__number_of_hits == self.__size:
                self.__sunk = True
            return 0
        else:
            return -1

    def is_sunk(self) -> bool:
        return self.__sunk

    def get_size(self) -> bool:
        return self.__size


