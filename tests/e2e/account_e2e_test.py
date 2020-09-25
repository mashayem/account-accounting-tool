import json
import os
import subprocess
import json


def run_app_with_file(filename):
    executable_path = os.getenv('EXECUTABLE_PATH', 'dist/macos/account')

    output = subprocess.check_output([
        executable_path,
        filename
    ])

    return json.loads(output.decode('ascii'))


def test_with_valid_file_balance_positive_only():
    parsed_output = run_app_with_file('tests/fixtures/only-positive-balance-373-records.txt')

    assert parsed_output['total_transactions'] == 373
    assert parsed_output['balance'] == 7910.0
    assert parsed_output['first_negative_transaction_date'] == ''
    assert parsed_output['first_negative_transaction_balance'] == ''


# verify balance is calculated correctly
def test_calculate_balance():
    parsed_output = run_app_with_file('tests/fixtures/account_data_100_records.txt')

    assert parsed_output['balance'] == 1695.64


def test_count_transactions():
    parsed_output = run_app_with_file('tests/fixtures/account_data_100_records.txt')

    assert parsed_output['total_transactions'] == 100


def test_file_not_found_shows_relevant_error_message():
    parsed_output = run_app_with_file('tests/fixtures/non_existent_file.txt')
    assert parsed_output['error'] == 'file not found'


def test_process_empty_file_shows_relevant_error_message():
    parsed_output = run_app_with_file('tests/fixtures/empty.txt')
    assert parsed_output['error'] == 'file is empty'


def test_process_file_with_empty_line_shows_relevant_error_message():
    parsed_output = run_app_with_file('tests/fixtures/empty_line.txt')
    assert parsed_output['error'] == 'error on line #6: invalid line format: ' \
                                     'expected \'mm-dd-yyyy Deposit $xx.xx\' ' \
                                     'or \'mm-dd-yyyy Withdraw $xx.xx\', found \'\n\''


def test_process_file_with_invalid_date_shows_relevant_error_message():
    parsed_output = run_app_with_file('tests/fixtures/invalid_date.txt')
    assert parsed_output['error'] == 'error on line #5: invalid date: found 09-20-202, expected format: mm-dd-yyyy'


def test_process_file_with_invalid_transaction_type_shows_relevant_error_message():
    parsed_output = run_app_with_file('tests/fixtures/invalid_transaction_type.txt')
    assert parsed_output['error'] == "error on line #5: invalid transaction type: " \
                                     "found 'Withdraws', expected: 'Withdraw' or 'Deposit'"


def test_process_file_with_invalid_amount_shows_relevant_error_message():
    parsed_output = run_app_with_file('tests/fixtures/invalid_amount.txt')
    assert parsed_output['error'] == 'error on line #6: invalid amount: found $110, expected format: $xx.xx'


# verify it is indicated properly when there was at least 1 occurrence of negative balance
def test_negative_balance_registered():
    parsed_output = run_app_with_file('tests/fixtures/account_data_100_records.txt')
    assert parsed_output['first_negative_transaction_date'] == '09-22-2020'
    assert parsed_output['first_negative_transaction_balance'] == -12.79


def test_negative_balance_not_overwritten_by_following_records():
    parsed_output = run_app_with_file('tests/fixtures/repeat_negative_balance_20_records.txt')
    assert parsed_output['first_negative_transaction_date'] == '09-29-2020'
    assert parsed_output['first_negative_transaction_balance'] == -1340.0


# 100,000 records
def test_big_file_processed_correctly():
    parsed_output = run_app_with_file('tests/fixtures/account_data_100_000_records.txt')
    assert parsed_output['total_transactions'] == 100000
    assert parsed_output['balance'] == -32270.0
    assert parsed_output['first_negative_transaction_date'] == '09-25-2020'
    assert parsed_output['first_negative_transaction_balance'] == -80.0

