def is_vertical(segment):
    ((x1, y1), (x2, y2)) = segment
    return (x1 == x2) and (y1 != y2)


def is_horizontal(segment):
    ((x1, y1), (x2, y2)) = segment
    return (y1 == y2) and (x1 != x2)


def is_degenerated(segment):
    ((x1, y1), (x2, y2)) = segment
    return (x1 == x2) and (y1 == y2)


def is_inclined(segment):
    if (not is_horizontal(segment) and (not is_vertical(segment)) and (not is_degenerated(segment))):
        return True
    else:
        return False

'''

def is_degenerated(line):
    p1, p2 = line
    return p1 == p2


def is_inclined(line):
    return not (
        is_vertical(line) or is_horizontal(line) or is_degenerated(line)
    )

'''


line1 = (0, 10), (100, 130)
print is_vertical(line1) # False
print is_horizontal(line1) # False
print is_degenerated(line1) # False
print is_inclined(line1) # True

line2 = (42, 1), (42, 2)
print is_vertical(line2) # True

line3 = (100, 50), (200, 50)
print is_horizontal(line3) # True