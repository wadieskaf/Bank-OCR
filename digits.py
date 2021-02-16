from DigitLCD import DigitLCD
import numpy as np

zero = np.full((3, 3), ' ', dtype=str)
zero[0] = list(' _ ')
zero[1] = list('| |')
zero[2] = list('|_|')
zero_digit = DigitLCD()
zero_digit.digit = zero

one = np.full((3, 3), ' ', dtype=str)
one[0] = list('   ')
one[1] = list('  |')
one[2] = list('  |')
one_digit = DigitLCD()
one_digit.digit = one

two = np.full((3, 3), ' ', dtype=str)
two[0] = list(' _ ')
two[1] = list(' _|')
two[2] = list('|_ ')
two_digit = DigitLCD()
two_digit.digit = two

three = np.full((3, 3), ' ', dtype=str)
three[0] = list(' _ ')
three[1] = list(' _|')
three[2] = list(' _|')
three_digit = DigitLCD()
three_digit.digit = three

four = np.full((3, 3), ' ', dtype=str)
four[0] = list('   ')
four[1] = list('|_|')
four[2] = list('  |')
four_digit = DigitLCD()
four_digit.digit = four

five = np.full((3, 3), ' ', dtype=str)
five[0] = list(' _ ')
five[1] = list('|_ ')
five[2] = list(' _|')
five_digit = DigitLCD()
five_digit.digit = five

six = np.full((3, 3), ' ', dtype=str)
six[0] = list(' _ ')
six[1] = list('|_ ')
six[2] = list('|_|')
six_digit = DigitLCD()
six_digit.digit = six

seven = np.full((3, 3), ' ', dtype=str)
seven[0] = list(' _ ')
seven[1] = list('  |')
seven[2] = list('  |')
seven_digit = DigitLCD()
seven_digit.digit = seven

eight = np.full((3, 3), ' ', dtype=str)
eight[0] = list(' _ ')
eight[1] = list('|_|')
eight[2] = list('|_|')
eight_digit = DigitLCD()
eight_digit.digit = eight

nine = np.full((3, 3), ' ', dtype=str)
nine[0] = list(' _ ')
nine[1] = list('|_|')
nine[2] = list(' _|')
nine_digit = DigitLCD()
nine_digit.digit = nine

a = np.full((3, 3), ' ', dtype=str)
a[0] = list(' _ ')
a[1] = list('|_|')
a[2] = list('| |')
a_digit = DigitLCD()
a_digit.digit = a

b = np.full((3, 3), ' ', dtype=str)
b[0] = list(' _ ')
b[1] = list('|_\\')
b[2] = list('|_/')
b_digit = DigitLCD()
b_digit.digit = b

c = np.full((3, 3), ' ', dtype=str)
c[0] = list(' _ ')
c[1] = list('|  ')
c[2] = list('|_ ')
c_digit = DigitLCD()
c_digit.digit = c

d = np.full((3, 3), ' ', dtype=str)
d[0] = list(' _ ')
d[1] = list('| \\')
d[2] = list('|_/')
d_digit = DigitLCD()
d_digit.digit = d

e = np.full((3, 3), ' ', dtype=str)
e[0] = list(' _ ')
e[1] = list('|_ ')
e[2] = list('|_ ')
e_digit = DigitLCD()
e_digit.digit = e

f = np.full((3, 3), ' ', dtype=str)
f[0] = list(' _ ')
f[1] = list('|_ ')
f[2] = list('|  ')
f_digit = DigitLCD()
f_digit.digit = f

all_numbers = [zero_digit, one_digit, two_digit, three_digit, four_digit, five_digit, six_digit, seven_digit,
               eight_digit, nine_digit, a_digit, b_digit, c_digit, d_digit, e_digit, f_digit]


def get_number(digit):
    for index, number in enumerate(all_numbers):
        if np.array_equal(number.digit, digit):
            return str(index)
    return '?'


def get_string(digit):
    for index, number in enumerate(all_numbers):
        if np.array_equal(number.digit, digit):
            if index <= 9:
                return str(index)
            else:
                return dec_to_hex[index]

    return '?'


dec_to_hex = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}
