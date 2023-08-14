# Initializing our (empty) blockchain list
blockchain = []

def get_last_blockchain_value():
	"""Returns the last value of the current blockchain."""
	return blockchain[-1]

# This Function accepts two arguments
# One required and one optional one
def add_value(transaction_amount,last_transaction=0):
	"""
    Append a value as well as the last blockchain value to the blockchain
    Arguments:
        :transaction_amount: The amount should be added
        :last_transaction: The last blockchain transaction (default [1]).
    """
	blockchain.append([last_transaction ,transaction_amount])


def get_user_input():
	"""
    Returns the input of the user (a new transaction amount) as float.
    """
	user_input = input('Your Transaction amount please: ')
	return user_input


# Get the first Transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(transaction_amount=tx_amount)

while True:
    print('Please Choose')
    print('1: Add a new transaction Value')
    print('2: Output the blocks')
    print('3: Quit')

    choice = int(input(''))
    if choice == 1:
        tx_amount = get_user_input()
        add_value(transaction_amount=tx_amount, last_transaction=get_last_blockchain_value())

# Get the second Transaction input and add the value to the blockchain
# tx_amount = get_user_input()
# add_value(transaction_amount=tx_amount, last_transaction=get_last_blockchain_value())

# Get the Third Transaction input and add the value to the blockchain
# tx_amount = get_user_input()
# add_value(transaction_amount=tx_amount, last_transaction=get_last_blockchain_value())


    elif choice == 3:
          break

    # Output the blockcain list to the console
    else:
        for block in blockchain:
            print('Outputing Block')
            print(block)
	
print('done')