from BankAccount import BankAccount


class Reader:
    def __init__(self):
        self.accounts = list()

    def parse_text_file(self, text_file):
        bank_account = BankAccount()
        for row_index, row in enumerate(text_file):
            if (row_index + 1) % 4 == 0:
                self.accounts.append(bank_account)
                bank_account = BankAccount()
            else:
                strip_row = row.rstrip()
                for digit_index, index in enumerate(range(0, len(strip_row), 3)):
                    value = list(strip_row[index:index + 3])
                    if len(value) < 3:
                        value.append(' ')
                    bank_account.set_row(digit_index=digit_index, row_index=row_index % 4, value=value)
