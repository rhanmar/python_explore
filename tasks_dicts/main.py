d = {
	'name': 'Dima',
	'age': 21,
	'is_student': True
}

key = 'test'
value = 100

d.setdefault(key, []).append(value)

print d

value = 200

d.setdefault(key, []).append(value)

print d


from collections import defaultdict

dd = defaultdict(int)
dd['a'] += 5

print dd

def new_value():
	return 100 
dn = defaultdict(new_value)
dn['a'] += 4
print dn

'''
print "name" in d
print 'aaa' in d

print d.get('asdg')
print d.get('age')

print d.keys()
print d.values()
print d.items()

for k, v in d.items():
	print k # tuples
	print v



l = [1,2,3]
for i in enumerate(l):
	print i # tuples
'''

'''
l1 = [1,2,3]
l2 = ['a', 'b', 1]
print l1 + l2
print((l1 + l2) is l1)
print((l1 + l2) is l2)
l3 = l1[:]
print l3 is l1
'''
