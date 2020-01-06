# high order funcitons

def call_twice(function, *args, **kwargs):
    first = function(*args, **kwargs) # unpack -> empty tuple -> works with shoot()
    second = function(*args, **kwargs)
    return (first, second)



def push_and_count(target, *, value):
    target.append(target)
    return len(target)

def shoot():
    return 'Bang!'

print(call_twice(push_and_count, [], value=42))
print(call_twice(shoot))