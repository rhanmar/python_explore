s = {1,2,3}
print s
print type(s)

em = set()
print em

print len(s)

l = [1,1,2]
print len(l)
print len(set(l))


s1 = {1,2}
s2 = s1
print s1 is s2
s3 = s1.copy()
print s1 is s3

s1.add(10)
print s2


d = {
	'name': 'dima',
	'age': 21
}

print set(d)


my_l = [1,2,3,4,5]
i = iter(my_l)
print set(i)
print set(i)
print set(i)
print set(i)