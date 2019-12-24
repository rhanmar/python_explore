'''
find binary sum
'''

def binary_sum(number1, number2):
	return format((int(number1, 2) + int(number2, 2)), 'b')


print(binary_sum('10', '1')) # 11
print(binary_sum('1101', '101')) # 10010