# -----------------------------------------
# Assignment 3
# Configurable Payment Processing System
# Using Strategy Design Pattern
# -----------------------------------------

# Strategy Classes

class CreditCard:
    def pay(self, amount):
        print("Payment of Rs.", amount, "done using Credit Card.")


class DebitCard:
    def pay(self, amount):
        print("Payment of Rs.", amount, "done using Debit Card.")


class UPI:
    def pay(self, amount):
        print("Payment of Rs.", amount, "done using UPI.")


class Cash:
    def pay(self, amount):
        print("Payment of Rs.", amount, "paid in Cash.")


# Context Class

class PaymentProcessor:

    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)


# ---------------- Main Program ----------------

amount = float(input("Enter Payment Amount: "))

print("\nSelect Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Cash")

choice = int(input("Enter your choice: "))

if choice == 1:
    method = CreditCard()

elif choice == 2:
    method = DebitCard()

elif choice == 3:
    method = UPI()

elif choice == 4:
    method = Cash()

else:
    print("Invalid Choice")
    exit()

payment = PaymentProcessor(method)
payment.process_payment(amount)