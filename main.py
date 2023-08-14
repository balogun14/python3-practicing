blockchain = []

def get_last_blockchain_value():
	return blockchain[-1]


def add_value(number,last_value=0):
	blockchain.append([last_value ,number])

	

add_value(2)
add_value(4,get_last_blockchain_value())
add_value(9, get_last_blockchain_value())

print(blockchain)
