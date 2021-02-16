from Reader import Reader
import utils

print('##### Story 1 #####')

reader = Reader()

accounts_file = open('./accounts.txt')

reader.parse_text_file(accounts_file)

print(reader.accounts[1].to_string())

print('##### Story 2 #####')

print(reader.accounts[1].check_sum())

print('##### Story 3 #####')
output_file = open('output.txt', 'w')

for account in reader.accounts:
    output_file.write(account.to_string() + ' ' + account.account_state() + '\n')

output_file.close()

print('Check the output.txt file')

print('##### Story 4 #####')

print(utils.fix_account_number(reader.accounts[0]))

print('##### Story 5 #####')

print('Support for Hexa characters added!')

print('#### Printing test')

print(reader.accounts[1])
print(reader.accounts[1].account_number[0])