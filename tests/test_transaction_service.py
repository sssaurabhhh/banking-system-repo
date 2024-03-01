import unittest
from Service.transaction_service import TransactionService
from Domain.account import Account
from Domain.customer import Customer

class TestTransactionService(unittest.TestCase):
    def test_make_deposit(self):
        customer = Customer(customer_id="1", name="Saurabh Singh", email="saurabh.jamia@gmail.com", phone_number="9999999999")
        account = Account(account_id="123", customer_id=customer.customer_id, account_number="987654", balance=1000)

        transaction_service = TransactionService()

        transaction_service.make_transaction(account, amount=500, transaction_type="deposit")

        self.assertEqual(account.get_balance(), 1500)

    def test_make_withdrawal(self):
        customer = Customer(customer_id="1", name="Saurabh Singh", email="saurabh.jamia@gmail.com", phone_number="9999999999")
        account = Account(account_id="123", customer_id=customer.customer_id, account_number="987654", balance=1000)

        transaction_service = TransactionService()

        transaction_service.make_transaction(account, amount=300, transaction_type="withdraw")

        self.assertEqual(account.get_balance(), 700)

    def test_invalid_transaction_type(self):
        customer = Customer(customer_id="1", name="Saurabh Singh", email="saurabh.jamia@gmail.com", phone_number="9999999999")
        account = Account(account_id="123", customer_id=customer.customer_id, account_number="987654", balance=1000)

        transaction_service = TransactionService()

        with self.assertRaises(ValueError):
            transaction_service.make_transaction(account, amount=200, transaction_type="invalid_type")