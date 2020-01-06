# closures

def partial_apply(func, first_arg):
    def inner(second_arg):
        return func(first_arg, second_arg)
    return inner

def flip(func):
    def inner(first_arg, second_arg):
        return func(second_arg, first_arg)
    return inner

'''
partial_apply принимает функцию от двух аргументов и первый аргумент, а возвращает замыкание — функцию, 
которая примет второй аргумент и наконец применит замкнутую функцию к обоим аргументам (и вернёт результат).

Функция flip принимает в качестве единственного аргумента функцию от двух аргументов. 
Возвращаемое замыкание должно также принять два аргумента, а затем применить к ним замкнутую функцию, 
но аргументы подставить в обратном порядке. Таким образом flip как бы "переворачивает" ("flips") исходную функцию.
'''

# test

def greet(name, surname):
    return f'Hello, {name} {surname}!'

f = partial_apply(greet, 'Dorian')
print (f('Grey'))


f = flip(greet)
print (f('Christian', 'Teodor'))
