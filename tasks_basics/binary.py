'''
decimal to binary
'''

def binary(number):
	if number == 0:	return '0'
	if number == 1: return '1'
	
	result = ''
	modulo = 0	

	while number > 0:
		modulo = number % 2
		result = str(modulo) + result
		number = number // 2

	return result	


print(binary(10))
print(binary(0))
print(binary(1))