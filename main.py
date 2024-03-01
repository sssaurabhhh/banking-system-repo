from Service.account_service import AccountService
from Service.transaction_service import TransactionService
from Service.statement_service import StatementService
from Infra.account_repository import AccountRepository
from Domain.customer import Customer

if __name__ == '__main__':
    account_service = AccountService()
    transaction_service = TransactionService()
    statement_service = StatementService()
    account_repository = AccountRepository()

    # Create a new account
    customer = Customer(customer_id="1", name="John Doe", email="john@example.com", phone_number="1234567890")
    account = account_service.create_account(customer_id=customer.customer_id, name=customer.name,
                                             email=customer.email, phone_number=customer.phone_number)
    account_repository.save_account(account)

    # Make a transaction
    transaction_service.make_transaction(account=account, amount=100, transaction_type="deposit")

    # Generate account statement
    statement = statement_service.generate_account_statement(account=account)
    print(statement)