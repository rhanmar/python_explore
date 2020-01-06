# keyword arguments

def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)


def get_colors():
	return {
	'red': rgb(red=255),
	'green': rgb(green=255),
	'blue': rgb(blue=255)
	}

colors = get_colors()
print(set(colors.keys()) == {'red', 'green', 'blue'}) # True
print (colors['red']) # 'rgb(255, 0, 0)'
print (colors['blue']) # 'rgb(0, 0, 255)'