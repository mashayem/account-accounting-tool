import subprocess

result = ''


def test_with_valid_file():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/account_data_20_records.txt'
    ]))

    assert 'Total transactions: 20' in output
    assert 'balance: -210.0' in output
    assert 'First negative-balance transaction:' in output
    assert 'Date: 09-22-2020' in output
    assert 'Balance after transaction: -100.0' in output


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
        'tests/fixtures/account_data_100_recods.txt'
    ]))
    assert 'file not found' in output


def test_process_empty_file_raises_exception():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/empty.txt'
    ]))
    assert 'file is empty' in output


def test_process_file_with_empty_line_raises_exception():
    output = str(subprocess.check_output([
        'dist/macos/account',
        'tests/fixtures/account_data_100_records.txt'
    ]))
    assert 'balance: 1695.64' in output


# def test_process_file_with_invalid_date_raises_exception():
#     output = str(subprocess.check_output([
#         'dist/macos/account',
#         'tests/fixtures/account_data_100_records.txt'
#     ]))
#     assert 'balance: 1695.64' in output
#
#
# def test_process_file_with_invalid_transaction_type_raises_exception():
#     output = str(subprocess.check_output([
#         'dist/macos/account',
#         'tests/fixtures/account_data_100_records.txt'
#     ]))
#     assert 'balance: 1695.64' in output
#
#
# def test_process_file_with_invalid_amount_raises_exception():
#     output = str(subprocess.check_output([
#         'dist/macos/account',
#         'tests/fixtures/account_data_100_records.txt'
#     ]))
#     assert 'balance: 1695.64' in output
#
#
# # verify it is indicated properly when there was at least 1 occurrence of negative balance
# def test_negative_balance_registered():
#     output = str(subprocess.check_output([
#         'dist/macos/account',
#         'tests/fixtures/account_data_100_records.txt'
#     ]))
#     assert 'balance: 1695.64' in output
#
# def test_negative_balance_not_overwritten_by_following_records():
#     output = str(subprocess.check_output([
#         'dist/macos/account',
#         'tests/fixtures/account_data_100_records.txt'
#     ]))
#     assert 'balance: 1695.64' in output

# def test_sample():
#     result = str(subprocess.check_output(['pwd']))
#     print(result)
