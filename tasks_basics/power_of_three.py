def is_power_of_three(number):

	i = 1
	while i < number:
		i *= 3
	return i == number



print is_power_of_three(1) # True
print is_power_of_three(2) # False
print is_power_of_three(9) # True