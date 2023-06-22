from oop_testing import Account, AccountType
import pytest


@pytest.fixture
def current_account():
    return Account(AccountType.DEPOSIT)


def test_current_account_initial_balance(current_account):
    with pytest.raises(AssertionError):
        assert current_account.get_balance() == 65


def test_current_account(current_account):
    current_account.deposit_money(67)
    assert current_account.get_balance() == 67


def test_current_account_negativ(current_account):
    current_account.deposit_money(-32)
    with pytest.raises(AssertionError):
        assert current_account.get_balance() == 32


def test_current_account_str(current_account):
    current_account.deposit_money(400)
    with pytest.raises(AssertionError):
        assert current_account.get_balance() == "400"
