name = input("what is your name: ")
age = input("how old are you: ")


def person(name,age):
	result =  name + ' ' + age
	print(result)

def decade_calculator(age):
	number_of_decades = int(age) // 10
	print('you\'ve lived for ' + str(number_of_decades) + ' decade')

person(name,age)

decade_calculator(age)
