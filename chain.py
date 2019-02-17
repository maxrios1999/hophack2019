import base64


class Wallet:
    number = 1

    def __init__(self):
        self.balance = 0
        self.private_key = Wallet.number
        Wallet.number += 1

    @property
    def balance(self):
        return self.balance

    @balance.setter
    def set_balance(self, balance):
        self.balance = balance

    @property
    def private_key(self):
        return self.private_key

    @private_key.setter
    def set_private_key(self, private_key):
        self.private_key = private_key

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= amount
        else:
            raise Exception("Balance is too low.")

    def deposit(self, amount):
        self.balance += amount


class Block:

    def __init__(self, transaction):
        self.block_data.append(transaction)
        self.encode_block = ""
        self.decode_block = ""
        self.isEncoded = False

    def append_block_data(self, transaction):
        if len(self.block_data)< 20:
            self.block_data.append(transaction)
        else:
            if self.next_block is None:
                while not self.encode_block():

                    self.next_block = Block(transaction)

            else:
                self.next_block.append_block_data(transaction)

    def encode_block(self):
        for x in self.block_data:
            self.encode_block += x
        isEncoded = True
        return base64.b64encode(self.encrypted_block)

    def decode_block(self):
        if self.isEncoded:
            return base64.b64decode()
        else:
            raise Exception("Block not encoded.")


class Transaction:

    def __init__ (self, sender, receiver, amount):
        self.sender = sender.get_private_key()
        self.receiver = receiver.get_private_key()
        self.amount = amount

    @property
    def sender(self):
        return self.sender

    @sender.setter
    def get_sender(self, sender):
        self.sender = sender

    @property
    def receiver(self):
        return self.receiver

    @receiver.setter
    def get_receiver(self, receiver):
        self.receiver = receiver

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def set_amount(self, amount):
        self.amount = amount

    def add_transaction(self):
        Block(self)

while True:

    blocks = []
    blocks.append(Block(Transaction(None,"total",100)))
    last = blocks[-1]
    # tans
    newT =None
    if len(last) !=20:
        last.append_block_data(newT)
    else:
        newBloc = Block(newT)
        last.decode_block()
        blocks.append(newBloc.encode_block())