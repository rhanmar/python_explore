def make_user(name, age):
	return {'name': name, 'age': age}

def format_user(data):
	return "{}, {}".format(data['name'], data['age'])


phil = make_user('Phil', 25)
print type(phil) # <class 'dict'>
print format_user(phil) # 'Phil, 25'