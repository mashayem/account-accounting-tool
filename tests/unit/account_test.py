import pytest
from src.main import process_account_data

# paths to sample files with transactions
negative_balance_path = 'tests/fixtures/negative_balance_sample.txt'
negative_balance_single_occurrence_path = 'tests/fixtures/single_occurrence_of_negative_balance_sample.txt'
empty_file_path = 'tests/fixtures/empty.txt'
empty_line_path = 'tests/fixtures/empty_line.txt'
invalid_date_path = 'tests/fixtures/invalid_date.txt'
invalid_transaction_type_path = 'tests/fixtures/invalid_transaction_type.txt'
invalid_amount_path = 'tests/fixtures/invalid_amount.txt'


# verify balance is calculated correctly
def test_calculate_balance():
    transaction_data = process_account_data(negative_balance_path)
    balance_actual = transaction_data[1]
    balance_expected = -100.00
    assert balance_actual == balance_expected


# verify total number of transactions is counted correctly
def test_count_transactions():
    transaction_data = process_account_data(negative_balance_path)
    count_actual = transaction_data[0]
    count_expected = 2
    assert count_actual == count_expected


def test_file_not_found_raises_exception():
    with pytest.raises(FileNotFoundError) as e:
        process_account_data('random/broken/path')
    assert 'No such file or directory' in str(e.value)


def test_process_empty_file_raises_exception():
    with pytest.raises(ValueError) as e:
        process_account_data(empty_file_path)
    assert 'file is empty' in str(e.value)


def test_process_file_with_empty_line_raises_exception():
    with pytest.raises(ValueError) as e:
        process_account_data(empty_line_path)
    # assert "expected" == "actual"
    assert 'error on line #6: ' \
           'invalid line format: ' \
           'expected \'mm-dd-yyyy Deposit $xx.xx\' or \'mm-dd-yyyy Withdraw $xx.xx\', ' \
           'found \'\n\'' in str(e.value)


def test_process_file_with_invalid_date_raises_exception():
    with pytest.raises(ValueError) as e:
        process_account_data(invalid_date_path)
    assert 'error on line #5: ' \
           'invalid date: found 09-20-202, ' \
           'expected format: mm-dd-yyyy' in str(e.value)


def test_process_file_with_invalid_transaction_type_raises_exception():
    with pytest.raises(ValueError) as e:
        process_account_data(invalid_transaction_type_path)
    assert 'error on line #5: invalid transaction type: found \'Withdraws\', ' \
           'expected: \'Withdraw\' or \'Deposit\'' in str(e.value)


def test_process_file_with_invalid_amount_raises_exception():
    with pytest.raises(ValueError) as e:
        process_account_data(invalid_amount_path)
    assert 'error on line #6: invalid amount: found $110, expected format: $xx.xx' in str(e.value)


# verify it is indicated properly when there was at least 1 occurrence of negative balance
def test_negative_balance_registered():
    transaction_data = process_account_data(negative_balance_single_occurrence_path)
    status_actual = transaction_data[2]
    status_expected = True
    assert status_actual == status_expected
