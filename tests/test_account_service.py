import unittest
from Service.account_service import AccountService
from Domain.customer import Customer


class TestAccountService(unittest.TestCase):
    def test_create_account(self):
        account_service = AccountService()
        customer = Customer(customer_id="1", name="Saurabh Singh", email="saurabh.jamia@gmail.com", phone_number="9999999999")
        account = account_service.create_account(customer_id=customer.customer_id, name=customer.name,
                                                email=customer.email, phone_number=customer.phone_number)
        self.assertIsNotNone(account)
