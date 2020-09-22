import datetime

import random
import sys


def generate_records(records_num):
    start_date = datetime.datetime.today()
    date_range = (start_date + datetime.timedelta(days=counter) for counter in range(records_num))
    record_types = ['Withdraw', 'Deposit']

    with open(f'account_data_{records_num}_records.txt', 'w') as f:
        for date in date_range:
            record_date = date.strftime('%m-%d-%Y')
            record_type = random.choice(record_types)
            record_amount = '${:.2f}'.format(random.randint(1, 15) * 10)

            f.write(f'{record_date} {record_type} {record_amount}\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        records_num = int(sys.argv[1])
    else:
        records_num = 10

    generate_records(records_num)