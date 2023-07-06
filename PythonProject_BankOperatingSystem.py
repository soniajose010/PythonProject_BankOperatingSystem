'''
Write a python program to replicate a Banking system. The following features are mandatory:
1.Account login
2. Amount Depositing
3. Amount Withdrawal
Other than the above features you can add any other also.
'''

class BankAccount:
    def __init__(self, login_details, balance=0):
        self.login_details = login_details
        self.balance = balance

    def login(self, entered_username, entered_password):
        if entered_username in self.login_details['username']:
            username_index = self.login_details['username'].index(entered_username)
            if entered_password == self.login_details['password'][username_index]:
                print("Login Successful\nWelcome to the Banking System")
                while True:
                    print("1. Deposit\n2. Withdrawal\n3. Balance Check\n4. Exit")
                    choice = int(input("Please enter your choice:"))
                    if choice == 1:
                        self.deposit()
                    elif choice == 2:
                        self.withdrawal()
                    elif choice == 3:
                        print("Your available balance:", self.balance)
                    elif choice == 4:
                        print("Thanks for using our banking system.")
                        break
                    else:
                        print("Invalid option")
            else:
                print("Login failed. Please enter a valid username and password")

    def deposit(self):
        amount = float(input("Enter the amount to be deposited: "))
        self.balance += amount
        print("Amount deposited:", amount)
        print("New balance:", self.balance)

    def withdrawal(self):
        amount = float(input("Enter the amount to be withdrawn: "))
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("New balance:", self.balance)


login_details = {
    "username": ['sonia', 'manu', 'arya','priya'],
    "password": ['sonia123', 'manu265', 'arya1990','priya234']
}


User1 = BankAccount(login_details)

#  username and password
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

# Login for User1
User1.login(entered_username, entered_password)