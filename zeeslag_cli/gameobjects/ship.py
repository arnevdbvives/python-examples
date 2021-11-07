class Ship():

    def __init__(self, positions):
        """ Posities is een rij van tuples met de posities in de oceaan"""
        self.__positions = positions
        self.__sunk = False
        self.__size = len(positions)
        self.__number_of_hits = 0

    def get_positions(self):
        return self.__positions

    def throw_bomb(self, position):
        """ position is a tuple with a position in the grid
            return 0 is there is a hit, -1 if there is no hit
        """
        if position in self.__positions:
            self.__number_of_hits += 1
            if self.__number_of_hits == self.__size:
                self.__sunk = True
            return 0
        else:
            return -1

    def is_sunk(self):
        return self.__sunk

    def get_size(self):
        return self.__size


