class Bank:
    title = "US Bank"
    def __init__(self, customer_name, current_balance, minimum_balance, routing_number):
            self.customer_name = customer_name
            self.current_balance = current_balance
            self.minimum_balance = minimum_balance
            self._routing_number = routing_number

            ##print("ERROR: current balance must be greater than or equal to minimum balance.")

    def deposit(self, amount):
        self.current_balance += amount
        print("success")

    def withdraw(self, amount):
        if (self.current_balance - amount) >= self.minimum_balance:
            if isinstance(self, Checking_account):
                if amount > self.transfer_limit:
                    print("Transfer limit exceeded. Unable to complete.")
                else:
                    self.current_balance -= amount
                    print("Withdrawal successful")
            else:
                self.current_balance -= amount
                print("Withdrawal successful")
        else:
            print("Insufficient funds")

    def print_customer_information(self):
        print("Customer name: ", self.customer_name)
        print("Current balance: ", self.current_balance)
        print("Minimum balance: ", self.minimum_balance)

class Savings_account(Bank):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, routing_number)
        self.__account_number = account_number
        self.interest_rate = interest_rate

class Checking_account(Bank):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, routing_number)
        self.__account_number = account_number
        self.transfer_limit = transfer_limit



