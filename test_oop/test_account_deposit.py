from oop_testing import Account, AccountType
import pytest

@pytest.fixture
def deposit_account():
    return Account(AccountType.DEPOSIT)

def test_deposit(deposit_account):
    with pytest.raises(TypeError):
        assert deposit_account.balance() == 6

def test_deposit_account_deposit(deposit_account):
    deposit_account.deposit_money(20)
    assert deposit_account.get_balance() == 20


def test_deposit_account_deposit_amount(deposit_account):
    deposit_account.deposit_money(866)
    with pytest.raises(AssertionError):
        assert deposit_account.get_balance() == 0


def test_deposit_account_deposit_negative(deposit_account):
    deposit_account.deposit_money(-866)
    with pytest.raises(AssertionError):
        assert deposit_account.get_balance() == 0


def test_deposit_account_deposit_float(deposit_account):
    deposit_account.deposit_money(54)
    assert deposit_account.get_balance() == 54,1