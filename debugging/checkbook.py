class Checkbook:
    def __init__(self):
        self.balance = 0.0  # Initialize the balance to zero

    def deposit(self, amount):
        """
        Adds the specified amount to the balance.

        Parameters:
            amount (float): The amount to deposit. Must be a positive number.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Deducts the specified amount from the balance if sufficient funds are available.

        Parameters:
            amount (float): The amount to withdraw. Must be positive and less than or equal to the balance.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Displays the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()  # Create an instance of Checkbook
    while True:
        try:
            # Prompt the user for an action
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
            if action == 'exit':
                print("Exiting the program. Goodbye!")
                break
            elif action == 'deposit':
                amount = float(input("Enter the amount to deposit: $"))  # Read deposit amount
                cb.deposit(amount)
            elif action == 'withdraw':
                amount = float(input("Enter the amount to withdraw: $"))  # Read withdrawal amount
                cb.withdraw(amount)
            elif action == 'balance':
                cb.get_balance()  # Display the current balance
            else:
                print("Invalid command. Please try again.")  # Handle invalid commands
        except ValueError:
            print("Invalid input. Please enter a numeric value where required.")  # Handle non-numeric input


if __name__ == "__main__":
    main()