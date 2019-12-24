def is_palindrome(str):
	#if len(str) == 1:
	#	return True
	result = ''
	i = len(str) - 1
	while i >= 0:
		result += str[i]
		i -= 1
	return str == result

def is_palindrome2(str):
	result = '';
	end = len(str) - 1;
	start = 0
	while (end - start) > 0:
		if str[start] != str[end]:
			return False
		start += 1
		end -= 1
	return True

print(is_palindrome('radar'))  # True
print(is_palindrome('a'))      # True
print(is_palindrome('abs'))    # False

print(is_palindrome2('radar'))  # True
print(is_palindrome2('a'))      # True
print(is_palindrome2('abs'))    # False