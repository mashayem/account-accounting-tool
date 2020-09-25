import subprocess

result = ''


def test_with_valid_file_balance_positive_only():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/only-positive-balance-373-records.txt'
    ]))

    assert 'Total transactions: 373' in output
    assert 'balance: 7910.0' in output
    assert 'First negative-balance transaction:' not in output
    assert 'Date:' not in output
    assert 'Balance after transaction:' not in output


# verify balance is calculated correctly
def test_calculate_balance():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/account_data_100_records.txt'
    ]))
    assert 'balance: 1695.64' in output


def test_sample():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/account_data_100_records.txt'
    ]))
    assert 'balance: 1695.64' in output


def test_count_transactions():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/account_data_100_records.txt'
    ]))
    assert 'Total transactions: 100' in output


def test_file_not_found_raises_exception():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/account_data_100_recordss.txt'
    ]))
    assert 'file not found' in output


def test_process_empty_file_raises_exception():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/empty.txt'
    ]))
    assert 'file is empty' in output


# todo: rename tests - error, not exception in e2e tests
def test_process_file_with_empty_line_raises_exception():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/empty_line.txt'
    ]))
    assert 'error on line #6: invalid line format: ' \
           'expected "mm-dd-yyyy Deposit $xx.xx" or "mm-dd-yyyy Withdraw $xx.xx"' in output


def test_process_file_with_invalid_date_raises_exception():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/invalid_date.txt'
    ]))
    assert 'error on line #5: invalid date: found 09-20-202, expected format: mm-dd-yyyy' in output


def test_process_file_with_invalid_transaction_type_raises_exception():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/invalid_transaction_type.txt'
    ]))
    assert 'error on line #5: invalid transaction type: found "Withdraws",' \
           ' expected: "Withdraw" or "Deposit"' in output


def test_process_file_with_invalid_amount_raises_exception():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/invalid_amount.txt'
    ]))
    assert 'error on line #6: invalid amount: found $110, expected format: $xx.xx' in output


# verify it is indicated properly when there was at least 1 occurrence of negative balance
def test_negative_balance_registered():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/account_data_100_records.txt'
    ]))
    assert 'First negative-balance transaction:' in output
    assert 'Date: 09-22-2020' in output
    assert 'Balance after transaction: -12.79' in output


def test_negative_balance_not_overwritten_by_following_records():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/repeat_negative_balance_20_records.txt'
    ]))
    assert 'Date: 09-29-2020' in output
    assert 'Balance after transaction: -1340.0' in output


# 100,000 records
def test_big_file_processed_correctly():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/account_data_100_000_records'
    ]))
    assert 'Total transactions: 100000' in output
    assert 'balance: -32270.0' in output
    assert 'Date: 09-25-2020' in output
    assert 'Balance after transaction: -80.0' in output


