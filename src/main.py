import re
import typer


def process_account_data(filename):
    balance = 0.00
    total_transactions = 0
    negative_occurred = False
    first_negative_transaction_date = ''
    first_negative_transaction_balance = ''

    with open(filename, 'r') as transactions:
        for line_counter, line in enumerate(transactions, start=1):
            try:
                date, transaction_type, amount = parse(line)
            except ValueError as e:
                raise ValueError(f'error on line #{line_counter}: {e}')

            balance += amount

            if balance < 0.00 and not negative_occurred:
                first_negative_transaction_date = date
                first_negative_transaction_balance = balance
                negative_occurred = True

            total_transactions = line_counter

    if total_transactions == 0:
        raise ValueError('file is empty')
    return total_transactions, balance, negative_occurred, \
           first_negative_transaction_date, first_negative_transaction_balance


def parse(line: str) -> tuple:
    tokens = line.split()

    if len(tokens) != 3:
        raise ValueError(
            'invalid line format:' +
            ' expected "mm-dd-yyyy Deposit $xx.xx" or "mm-dd-yyyy Withdraw $xx.xx", found' +
            f' "{line}"'
        )

    # validate date
    date = tokens[0]
    if re.match(r'^\d\d-\d\d-\d\d\d\d$', date) is None:
        raise ValueError(f'invalid date: found {date}, expected format: mm-dd-yyyy')

    # validate transaction type
    transaction_type = tokens[1]
    if re.match(r'^(Withdraw|Deposit)$', transaction_type) is None:
        raise ValueError(f'invalid transaction type: found "{transaction_type}", expected: "Withdraw" or "Deposit"')

    # validate amount
    amount = tokens[2]
    if re.match(r'^\$\d{1,8}\.\d\d$', amount) is None:
        raise ValueError(f'invalid amount: found {amount}, expected format: $xx.xx')

    amount = float(amount[1:])

    if transaction_type == 'Withdraw':
        amount *= -1

    return date, transaction_type, amount


def output_transaction_data(filename: str):
    try:
        total_transactions, balance, negative_occurred, \
        first_negative_transaction_date, first_negative_transaction_balance = process_account_data(filename)
    except ValueError as e:
        print(f'could not process file due to error:\n{e}')
        return
    except FileNotFoundError:
        print("file not found")
        return

    print('Total transactions: ' + str(total_transactions))
    print('balance: ' + str(balance))
    if negative_occurred:
        print("-" * 50)
        print('First negative-balance transaction:')
        print(f'Date: {first_negative_transaction_date}')
        print(f'Balance after transaction: {first_negative_transaction_balance}')


def main():
    typer.run(output_transaction_data)


if __name__ == '__main__':
    main()
