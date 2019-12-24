def rotate_left(triple):
    (a, b, c) = triple
    return (b, c, a)


def rotate_right(triple):
    (a, b, c) = triple
    return (c, a, b)


triple = ('A', 'B', 'C')
print rotate_left(triple) # ('B', 'C', 'A')
print rotate_right(triple) # ('C', 'A', 'B')