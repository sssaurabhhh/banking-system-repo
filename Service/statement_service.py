class StatementService:
    def generate_account_statement(self, account):
        return f"Account Statement for Account {account.account_number}:\nBalance: {account.get_balance()}"
