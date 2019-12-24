def find_num(source):
	for item in source:
		if (item > 1 and item % 2):
			return item


l = [1,2,3,4,5,6,7]
numbers = range(0, 10, 1)
print numbers
print l
i = iter(l)
print next(i)
print next(i)

test = list(i)
print test

'''
l = [1,2,3,4,5]
print id(l[1])
l[1] += 10
print l
print id(l[1])
print id(l[2])
print id(l[3])
print id(l[4])
'''

'''
numbers = range(3,11,2)
#test = range(10)
print numbers

i1 = iter(numbers)
print i1
print next(i1)
print next(i1)
print next(i1)
print next(i1)

i2 = iter(numbers)
print i2
print next(i2)
print next(i2)
print next(i2)
print next(i2)
print next(i2)
print next(i2)
'''
'''
l = enumerate("abcdefg")
print l
print list(l)
print list(l)

t = (1,0)
s = "abc"
r = range(10)

z = zip(t,s, r)
print list(z)
print z
list(z)
list(z)
list(z)
list(z)
print list(z)
print list(z)
print list(z)
print list(z)
'''
#print list(numbers)
#print tuple(numbers)

#print test

'''
l = [1,2,3,4,5,6,7,8,9,10]
s = 'hello'

i = iter(l)
i2 = l.__iter__()
next(i2)
next(i2)
next(i2)
next(i2)

i_s = iter(s)


print find_num(i)
print find_num(i)
print find_num(i)
print find_num(i)
print find_num(i)

print find_num(i2)
print find_num(i2)
print find_num(i2)
print find_num(i2)
print find_num(i2)
print find_num(i2)

'''
'''
print i
print i2
print i_s

print next(i)
print next(i)
print next(i)
print next(i)
print next(i)
print next(i)
'''