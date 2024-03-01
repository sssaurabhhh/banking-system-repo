class TransactionService:
    def make_transaction(self, account, amount, transaction_type):
        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")
