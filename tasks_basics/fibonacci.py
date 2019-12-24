'''
find fibonacci number by index
'''

def fib(index):
	if index <= 0:
		result = 0	# return 0
	elif index == 1:
		result = 1	#return 1
	else:
		result = fib(index - 1) + fib(index - 2)	# return ...
	return result


print(fib(0)) # 0
print(fib(1)) # 1
print(fib(2)) # 1
print(fib(3)) # 2
print(fib(4)) # 3
print(fib(5)) # 5
print(fib(10)) ## 55