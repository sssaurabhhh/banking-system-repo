from Domain.account import Account
from Domain.customer import Customer


class AccountService:
    def create_account(self, customer_id, name, email, phone_number):
        account = Account(account_id=None, customer_id=customer_id, account_number=str(hash(customer_id)), balance=0)
        return account