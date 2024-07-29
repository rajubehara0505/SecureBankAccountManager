class SecureBankAccount:
    def __init__(self, owner_name, initial_balance=0):
        """
        Initializes a SecureBankAccount object.

        Args:
            owner_name (str): The account holder's name.
            initial_balance (float, optional): Initial account balance. Defaults to 0.
        """
        self.owner_name = owner_name
        self.__balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): Amount to be deposited.

        Returns:
            bool: True if successful, False otherwise.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited ${amount} into your account.")
            self._display_balance()
            return True
        else:
            print("Please enter a positive amount to deposit.")
            return False

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account.

        Args:
            amount (float): Amount to be withdrawn.

        Returns:
            bool: True if successful, False otherwise.
        """
        if amount <= 0:
            print("Please enter a positive amount to withdraw.")
            return False
        elif amount > self.__balance:
            print("Insufficient balance to withdraw.")
            return False
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}.")
            self._display_balance()
            return True

    def _display_balance(self):
        """
        Displays the current balance.

        This method is intended for internal use.
        """
        print(f"Current balance for {self.owner_name}: ${self.__balance}")

# Example usage
if __name__ == "__main__":
    account = SecureBankAccount("Raju", 6000)
    account.deposit(3000)
    account.withdraw(1000)
    account.withdraw(7000)
