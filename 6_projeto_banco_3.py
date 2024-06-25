# Bank Project - Part 3 - Object Oriented Programming

from abc import ABC, abstractmethod


class Client:

    def __init__(self, address):
        self.address = address
        self.accounts = []

    def do_transactions(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)


class PhysicalPerson(Client):

    def __init__(self, id, name, birthdate, address):
        super().__init__(address)
        self.id = id
        self.name = name
        self.birthdate = birthdate


class Account:

    def __init__(self, number, client):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._history = History()

    def new_account(cls, client, number):
        return cls(number, client)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history

    def withdraw(self, value):
        ...

    def deposit(self, value):
        ...


class CurrentAccount(Account):

    def __init__(self, number, client, limit=500, withdraw_limit=3):
        super().__init__(number, client)
        self.limit = limit
        self.withdraw_limit = withdraw_limit

    def withdraw(self, value):
        ...

    # def deposit(self, value):
    # 	...


class History:

    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transactions(self, transaction):
        ...


class Transactions(ABC):

    @property
    @abstractmethod
    def value(self):
        ...

    @abstractmethod
    def register(self, account):
        ...


class Withdraw(Transactions):

    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value

    def register(self, account):
        ...


class Deposit(Transactions):

    def __init__(self, value):
        self._value = value

    def value(self):
        return self._value

    def register(self, account):
        ...
