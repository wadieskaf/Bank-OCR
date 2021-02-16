import numpy as np
import digits
import utils

def compare_digits(digit_1, digit_2):
    result = digit_1.digit != digit_2.digit
    return np.count_nonzero(result)


def check_sum(account_number):
    check_sum = 0
    account_number = account_number[::-1]
    for i, number in enumerate(account_number):
        check_sum += (i + 1) * int(number)
    if check_sum % 11 == 0:
        return True
    else:
        return False


def fix_account_number(bank_account):
    account_string = bank_account.to_number()
    if not bank_account.check_legibility():
        ill_index = account_string.find('?')
        ill_digit = bank_account.account_number[ill_index]
        alternatives = list()
        for number, digit in enumerate(digits.all_numbers):
            if compare_digits(ill_digit, digit) == 1:
                possible_account_number = list(account_string)
                if number > 9:
                    number = digits.dec_to_hex(number)
                else:
                    number = str(number)
                possible_account_number[ill_index] = number
                possible_account_number = "".join(possible_account_number)
                if check_sum(possible_account_number):
                    alternatives.append((ill_index, number))
        if len(alternatives) == 0:
            return 'ILL'
        elif len(alternatives) == 1:
            return 'This can be fixed!'
        else:
            return 'AMB'
    else:
        return 'This account has no missing character'


