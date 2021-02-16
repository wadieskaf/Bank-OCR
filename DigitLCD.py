import numpy as np


class DigitLCD:
    def __init__(self):
        self._digit = np.full((3, 3), ' ', dtype=str)

    def __str__(self):
        string = str()
        for row in range(3):
            string += '"' + "".join(list(self.return_row(row))) + '"' + '\n'
        return string

    def set_row(self, row_index, value):
        self._digit[row_index, :] = value

    def return_row(self, index):
        return self._digit[index, :]

    @property
    def digit(self):
        return self._digit

    @digit.setter
    def digit(self, digit_array):
        self._digit = digit_array
