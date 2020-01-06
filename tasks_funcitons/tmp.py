def one():
	x = ['one', 'two']
	def inner():
		print(x)
		print(id(x))
	return inner

o = one()
print(o)
o()

print(dir(o))
print((o.__closure__[0].cell_contents))

a = (o.__closure__[0].cell_contents)
print(id(a))


###

G = 10

def make_closure():
	a = 1
	b = 2
	def inner(x):
		print(b)
		return x + G + a
	return inner

print (make_closure()(2))



printers = []
for i in range(10):
	def make_printer(arg):
		def printer():
			print(arg)
		return printer

	p = make_printer(i)
	printers.append(p)




(printers[0]())
#9
(printers[5]())
#9
(printers[9]())
#9
#i = 42
#print (printers[0]())
#42

print (printers)