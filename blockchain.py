from hashlib import sha256
import random

blockchain = []
hash_list = []
last_hash

#returns the last transaction, if its the first block it returns 1
def get_last_value():
    if len(blockchain) == 0:
        return [1]
    return blockchain[-1]

#creates a hash to be able to verify each transaction
def create_hash():
    num = random.randint(1, 101)
    num = str(num)
    hash_list.append(sha256(num).hexdigest)

#adds the value to the blockchain
def add_value(new_amount):
    blockchain.append([get_last_value(), new_amount])

#checks to see if this is a valid transaction
def verify(self, signature, sender_address, transaction):
    if signature is sender_address:
        if transaction is self.transaction:
            return True
    return False

#asks the user for the amount they want to transfer
def ask_amount():
    return input("How much would you like to transfer: $")

#gets the previous transaction
def get_transaction():
    return get_last_value()

#returns the wallet balance and removes or adds funds 
def balance(wallet_balance = 0, amount_taken = 0, amount_received = 0):
    wallet_balance = wallet_balance - amount_taken
    wallet_balance = wallet_balance + amount_received
    return wallet_balance

#withdraws from the wallet
def withdraw(wallet_balance, amount_withdraw):
    wallet_balance = balance(wallet_balance, amount_withdraw)

#deposits to the wallet
def deposit(wallet_balance, amount_deposit):
    wallet_balance = balance(wallet_balance, amount_received = amount_deposit)

#continues to ask for amount until 'q' is inputted
while True:
    amount_transfer = ask_amount()
    if amount_transfer == 'q':
        break
    add_value(amount_transfer)
    create_hash()
    print(hash_list)
    print(blockchain)   