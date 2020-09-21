import pytest
from src.account import process_account_data, parse

# todo: take these out to a config file, do not keep tests data hardcoded in the tests file
# todo: create classes for Account and tests
filename_negative = 'tests/fixtures/negative_balance_sample.txt'
filename_negative_single_occurrence = 'tests/fixtures/single_occurrence_of_negative_balance_sample.txt'


# verify balance is calculated correctly
def test_calculate_balance():
    transaction_data = process_account_data(filename_negative)
    balance_actual = transaction_data[1]
    balance_expected = -100.00
    assert balance_actual == balance_expected


# verify total number of transactions is counted correctly
def test_count_transactions():
    transaction_data = process_account_data(filename_negative)
    count_actual = transaction_data[0]
    count_expected = 2
    assert count_actual == count_expected


# verify invalid files handled correctly
def test_parse_with_invalid_transaction_raises_exception():
    with pytest.raises(ValueError) as e:
        parse('09-1-2020 Withdraw $50.00')

    assert 'invalid date: found 09-1-2020, expected format: mm-dd-yyyy' in str(e.value)


# verify it is indicated properly when there was at least 1 occurrence of negative balance

def test_negative_balance_registered():
    transaction_data = process_account_data(filename_negative_single_occurrence)
    status_actual = transaction_data[2]
    status_expected = True
    assert status_actual == status_expected

# verify first negative transaction data not overwritten by the following negative-balance transactions

# verify big files are handled correctly (how to generate a REALLY big file)
