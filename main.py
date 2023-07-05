class Account:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Vklad ve výši {amount} Kč byl proveden.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Výběr ve výši {amount} Kč byl proveden.")
        else:
            print("Nedostatečný zůstatek na účtu.")

    def display_balance(self):
        print(f"Aktuální zůstatek na účtu {self.account_number} je {self.balance} Kč.")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            print("Účet s tímto číslem již existuje.")
        else:
            self.accounts[account_number] = Account(account_number, initial_balance)
            print(f"Účet s číslem {account_number} byl vytvořen.")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Účet s tímto číslem neexistuje.")
            return None


def main():
    bank = Bank()

    while True:
        print("\n******** Bankovní aplikace ********")
        print("1. Vytvořit nový účet")
        print("2. Vklad na účet")
        print("3. Výběr z účtu")
        print("4. Zobrazit zůstatek na účtu")
        print("5. Konec")

        choice = input("Zadejte číslo volby: ")

        if choice == "1":
            account_number = input("Zadejte číslo účtu: ")
            initial_balance = float(input("Zadejte počáteční zůstatek na účtu: "))
            bank.create_account(account_number, initial_balance)

        elif choice == "2":
            account_number = input("Zadejte číslo účtu: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Zadejte částku k vložení: "))
                account.deposit(amount)

        elif choice == "3":
            account_number = input("Zadejte číslo účtu: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Zadejte částku k výběru: "))
                account.withdraw(amount)

        elif choice == "4":
            account_number = input("Zadejte číslo účtu: ")
            account = bank.get_account(account_number)
            if account:
                account.display_balance()

        elif choice == "5":
            print("Děkujeme, že jste použili bankovní aplikaci. Ukončení programu.")
            break

        else:
            print("Neplatná volba. Zadejte číslo volby znovu.")


if __name__ == "__main__":
    main()
