class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount




class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    @staticmethod
    def iscorrupted(account: Account) -> bool:
        """
        How do we define if a bank account is corrupted? A corrupted bank account has:
        • an even number of attributes,
        • an attribute starting with b,
        • no attribute starting with zip or addr,
        • no attribute name, id and value,
        • name not being a string,
        • id not being an int,
        • value not being an int or a float.
        :return: True if is corrupted otherwise False
        """
        if len(account.__dict__) % 2 == 0:
            return True
        if any(elem[0] == 'b' for elem in account.__dict__):
            return True
        if not any(elem.startswith('zip') or elem.startswith('addr') for elem in account.__dict__):
            return True
        if not hasattr(account, "name") or not hasattr(account, "id") or not hasattr(account, "value"):
            return True
        if not isinstance(account.name, str) or not isinstance(account.id, int)\
                or not isinstance(account.value, (int, float)):
            return True
        return False

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error is occurred
        """
        if not isinstance(new_account, Account):
            print("Can't add new account, another type is detected")
            return False
        if hasattr(new_account, "name") and any(new_account.name == elem.name for elem in self.accounts):
            print("Error. Account name is already exists")
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin: str, dest: str, amount):
        """ Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if not isinstance(origin, str) or not isinstance(dest, str):
            print("Destination and origin account names must be strings")
            return False
        if not isinstance(amount, (int, float)):
            print("Can't transfer (amount is not a number)")
            return False
        dest_acc = None
        orig_acc = None
        for acc in self.accounts:
            if acc.name == dest:
                dest_acc = acc
            if acc.name == origin:
                orig_acc = acc
        if not dest_acc:
            print("Can't find destinator")
            return False
        if not orig_acc:
            print("Can't find origin")
            return False
        if amount < 0 or orig_acc.value < amount:
            print("Amount of transfer is negative or not enough money on origin acc")
            return False
        if Bank.iscorrupted(dest_acc) or Bank.iscorrupted(orig_acc):
            print("One of accounts is corrupted")
            return False
        dest_acc.transfer(amount)
        orig_acc.transfer(-amount)
        return True

    def fix_account(self, name: str) -> bool:
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            print("Name is not string")
            return False
        account = None
        for acc in self.accounts:
            if acc.name == name:
                account = acc
        if not account:
            print("Can't find name in accounts to fix it")
            return False
        for key in list(account.__dict__.keys()):
            if key[0] == 'b':
                delattr(account, key)
        if not any(elem.startswith('zip') for elem in account.__dict__):
            account.zip = "75017"
        if not any(elem.startswith('addr') for elem in account.__dict__):
            account.addr = "96 Bd Bessières"
        if not hasattr(account, "name") or not hasattr(account, "id") or not hasattr(account, "value"):
            return False
        if not hasattr(account, "value"):
            account.value = 0.0
        if not isinstance(account.name, str) or not isinstance(account.id, int)\
                or not isinstance(account.value, (int, float)):
            return False
        if len(account.__dict__) % 2 == 0:
            account.new_attr = "42"
        return True


if __name__ == '__main__':

    bank = Bank()
    bob = Account(
        name='Bob',
        brother="heyhey",
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation',
        lol="hihi"
    )
    bob2 = Account(
        name='Bob2',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation',
        lol="hihi"
    )
    bank.add(bob)
    bank.add(bob2)
    print(f"{bob.name} is corrupted {Bank.iscorrupted(bob)}")
    bank.fix_account(bob.name)
    print(f"{bob.name} is corrupted {Bank.iscorrupted(bob)}")

    print(f"{bob2.name} is corrupted {Bank.iscorrupted(bob2)}")
    bank.fix_account(bob2.name)
    print(f"{bob2.name} is corrupted {Bank.iscorrupted(bob2)}")

    print("\n\nThey are no John")
    bank.fix_account("John")

    print("\nCan't add (already added)")
    bank.add(bob)

    print("\nWrong type")
    bank.add("Harry")

    print(f"Bob1 money {bob.value}, Bob2 money {bob2.value}")
    print("Transfer 7k")
    bank.transfer(bob.name, bob2.name, 7000)

    print("\nGood amount dest not exists")
    bank.transfer(bob.name, "Potter", 7000)

    print("\nGood amount orig not exists")
    bank.transfer("Harry", bob2.name, 7000)

    print(f"Bob1 money {bob.value}, Bob2 money {bob2.value}")
    print("Ok transfer 1k")
    bank.transfer(bob.name, bob2.name, 1000)
    print(f"Bob1 money {bob.value}, Bob2 money {bob2.value}")
