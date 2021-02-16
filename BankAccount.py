from DigitLCD import DigitLCD
import digits


class BankAccount:
    def __init__(self):
        self._account_number = [DigitLCD() for _ in range(9)]

    @property
    def account_number(self):
        return self._account_number

    def __str__(self):
        string = str()
        for row in range(3):
            string += '" ' + " ".join(
                ["".join(list(digit.return_row(row))) for digit in self.account_number]) + ' "' + '\n'
        return string

    def set_row(self, digit_index, row_index, value):
        self.account_number[digit_index].set_row(row_index, value)

    def to_number(self):
        return "".join(digits.get_number(digit.digit) for digit in self.account_number)

    def to_string(self):
        return "".join(digits.get_string(digit.digit) for digit in self.account_number)

    def check_legibility(self):
        if '?' in self.to_number():
            return False
        else:
            return True

    def check_sum(self):
        if self.check_legibility():
            account_number = self.to_number()[::-1]
            check_sum = 0
            for i, number in enumerate(account_number):
                check_sum += (i + 1) * int(number)
            if check_sum % 11 == 0:
                return True
            else:
                return False
        else:
            return 'It has a missing character!'

    def account_state(self):
        if not self.check_legibility():
            return 'ILL'
        elif not self.check_sum():
            return 'ERR'
        else:
            return ''
