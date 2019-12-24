def diff(frist_angle, second_angle):
    first_diff = abs(frist_angle - second_angle)
    second_diff = (360 - abs(frist_angle - second_angle))
    return min(first_diff, second_diff)


'''

def diff(angle1, angle2):
    return min(
        abs(angle2 - angle1),
        abs(angle1 + 360 - angle2),
    )

''' 


print diff(0, 45) # 45
print diff(0, 180) # 180
print diff(120, 280) # 160
print diff(0, 190) #170