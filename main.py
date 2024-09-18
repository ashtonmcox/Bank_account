
from BankAccount import Bank
from BankAccount import Savings_account
from BankAccount import Checking_account


p1 = Bank("John", 100, 90, 123456789)
p2 = Bank("Sally", 100, 90, 987654321)


s1 = Savings_account("Alice", 500, 100, 111222333, 444555666, 3)
s2 = Savings_account("Bob", 200, 50, 222333444, 555666777, 4)

c1 = Checking_account("Eve", 300, 100, 333444555, 666777888, 2)
c2 = Checking_account("Charlie", 1000, 200, 444555666, 777888999, 1)

print("Creating a savings account for: Sam Kingston")
print(".....................................")
sam_savings = Savings_account("Sam", 1000, 100, 234234234234, 12345234, 5)
print("Account created successfully\nDetails: ")
sam_savings.print_customer_information()
print("\nCreating a checking account for Sam Kingston")
print(".....................................")
sam_checking = Checking_account("Sam", 250, 100, 2342342534, 12345234, 50)
print("Account created successfully\nDetails: ")
sam_checking.print_customer_information()
print("\nStarting $45 withdrawl")
print(".....................................")
sam_checking.withdraw(45)
print("Account details: ")
sam_checking.print_customer_information()


