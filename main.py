# Initializing our (empty) blockchain list
blockchain = []

def get_last_blockchain_value():
    """Returns the last value of the current blockchain."""
    if len(blockchain) <= 0:
        return None
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
    if last_transaction == None:
            last_transaction = [1]
    blockchain.append([last_transaction ,transaction_amount])


def get_user_input():
	"""
    Returns the input of the user (a new transaction amount) as float.
    """
	user_input = input('Your Transaction amount please: ')
	return user_input

def output_blocks():
      for block in blockchain:
            print('Outputing Block')
            print(block)


def verify_chain():
     block_index = 0
     is_valid = True
     for block in blockchain:
        if block_index ==0:
             block_index += 1
             continue
        elif block[0] == blockchain[block_index -1]:
               is_valid = True
               
        else:
               is_valid = False
               break
        block_index +=1
     return is_valid 
               
               


while True:
    print('Please Choose')
    print('1: Add a new transaction Value')
    print('2: Output the blocks')
    print('3: Quit')
    print('4: Manipulate the chain')

    choice = int(input(''))
    if choice == 1:
        tx_amount = get_user_input()
        add_value(transaction_amount=tx_amount, last_transaction=get_last_blockchain_value())


 # Output the blockcain list to the console
    elif choice == 2:
         output_blocks()

    elif choice == 3:
          break

    elif choice ==4:
         if len(blockchain) >= 1:
              blockchain[0] = [2]
    else:
        print('Input was Invalid  read the instructions again')
	
    if not verify_chain():
         print('Invalid BlockChain')
         break

print('done')


