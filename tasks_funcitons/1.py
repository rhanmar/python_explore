# positional args

def greet(first_name, *args):
	names = (first_name,) + args
	return "Hello, " + " and ".join(names)

def greet_2(first_name, *args):
	names = " and ".join((first_name,) + args)
	return "Hello, {}".format(names) 

print greet('Bob') # 'Hello, Bob!'
print greet('Moe', 'Mary') # 'Hello, Moe and Mary!'
print greet(*'ABC') # 'Hello, A and B and C!'


print greet_2('Bob') # 'Hello, Bob!'
print greet_2('Moe', 'Mary') # 'Hello, Moe and Mary!'
print greet_2(*'ABC') # 'Hello, A and B and C!'