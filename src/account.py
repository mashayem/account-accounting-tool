import re
import sys


def process_account_data(filename):
    balance = 0.00
    total_transactions = 0
    negative_occurred = False
    first_negative_transaction_date = ''
    first_negative_transaction_balance = ''

    with open(filename, 'r') as transactions:

        for line in transactions:
            date, transaction_type, amount = parse(line)

            balance += amount

            if balance < 0.00 and not negative_occurred:
                first_negative_transaction_date = date
                first_negative_transaction_balance = balance
                negative_occurred = True

            total_transactions += 1

    return total_transactions, balance, negative_occurred, \
        first_negative_transaction_date, first_negative_transaction_balance


def parse(line: str) -> tuple:
    tokens = line.split()
    print(line)

    if len(tokens) != 3:
        raise ValueError(f'invalid line: found {len(tokens)} tokens, expected 3: {line}')

    # validate date
    date = tokens[0]
    if re.match(r'\d\d-\d\d-\d\d\d\d', date) is None:
        raise ValueError(f'invalid date: found {date}, expected format: mm-dd-yyyy')

    # validate transaction type
    transaction_type = tokens[1]
    if re.match(r'(Withdraw|Deposit)', transaction_type) is None:
        raise ValueError(f'invalid transaction type: found {transaction_type}, expected: "Withdraw" or "Deposit"')

    # validate amount
    amount = tokens[2]
    if re.match(r'\$\d{1,8}\.\d\d', amount) is None:
        raise ValueError(f'invalid amount: found {amount}, expected format: $xx.xx')

    amount = float(amount[1:])

    if transaction_type == 'Withdraw':
        amount *= -1

    # todo: add validation of tokens with regexp

    return date, transaction_type, amount


#     raise Value


def output_transaction_data(filename):
    total_transactions, balance, negative_occurred, \
    first_negative_transaction_date, first_negative_transaction_balance = process_account_data(filename)

    print('Total transactions: ' + str(total_transactions))
    print('balance: ' + str(balance))
    if negative_occurred:
        print("-" * 50)
        print('First negative-balance transaction:')
        print(f'Date: {first_negative_transaction_date}')
        print(f'Balance after transaction: {first_negative_transaction_balance}')

    # ignore empty line
    # the date and balance for the first transaction that results in a negative account balance - do we need to sort the tr
    # transactions file by date
    # todo: sort transaction list by date
    # why do we need to show the first negative transaction - do we want to see the oldest one or the most recent one?

    # read file and parse line by line

    # withdraw or deposit

    # count transactions


if __name__ == '__main__':
    print(sys.argv)
    user_provided_filename = sys.argv[1]
    print(process_account_data(user_provided_filename))
