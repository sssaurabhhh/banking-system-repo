import unittest
from Service.statement_service import StatementService
from Domain.account import Account
from Domain.customer import Customer

class TestStatementService(unittest.TestCase):
    def test_generate_account_statement(self):
        customer = Customer(customer_id="1", name="Saurabh Singh", email="saurabh.jamia@gmail.com", phone_number="9999999999")
        account = Account(account_id="123", customer_id=customer.customer_id, account_number="987654", balance=1000)

        statement_service = StatementService()

        statement = statement_service.generate_account_statement(account)

        self.assertIsNotNone(statement)

        self.assertIn(f"Account Statement for Account {account.account_number}:", statement)
        self.assertIn(f"Balance: {account.get_balance()}", statement)