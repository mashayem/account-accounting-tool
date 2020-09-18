balance = 0.00
transaction_count = 0
transactions = open('transactions.txt', 'r')
is_negative_occur = False
first_negative_transaction_date = ''
first_negative_transaction_balance = ''

for line in transactions:
    if len(line) == 0:
        continue

    record = line.split()

    try:
        amount = float(record[2][1:])
    except IndexError:
        print(record)

    if record[1] == 'Withdraw':
        amount *= -1

    balance += amount
    if balance < 0.00 and not is_negative_occur:
        first_negative_transaction_date = record[0]
        first_negative_transaction_balance = balance
        is_negative_occur = True

    transaction_count += 1

print('Total transactions: ' + str(transaction_count))
print('balance: ' + str(balance))
if is_negative_occur:
    print('-' * 50 + '\nFirst negative-balance transaction:\nDate: {0}\nBalance after transaction: {1}'
          .format(first_negative_transaction_date, first_negative_transaction_balance))

# ignore empty line
# the date and balance for the first transaction that results in a negative account balance - do we need to sort the tr
# transactions file by date
# todo: sort transaction list by date
# why do we need to show the first negative transaction - do we want to see the oldest one or the most recent one?

# read file and parse line by line

# withdraw or deposit

# count transactions




