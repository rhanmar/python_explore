def printing(function):
     def inner(*args, **kwargs):
         result = function(*args, **kwargs)
         print('result =', result)
         return result
     return inner


@printing
def add_one(x):
     return x + 1

'''
print(add_one)

add_one = printing(add_one)
print(add_one)
y = add_one(10)
#result = 11
print (y) # 11

'''

@printing
def double(x):
	return x * x


a = add_one(10)
b = double(10)

c = printing(double)
print(c, c.__name__)
print(dir(c))