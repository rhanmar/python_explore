def greet(name):
	print("Hello, {}!".format(name))

print(__name__)


def main():
	greet("AAA")
	greet("BBB")

if __name__ == '__main__':
	main()