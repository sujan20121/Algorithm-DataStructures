def balance_check(s):

	if len(s)%2 != 0:
		return False

	opening = set('([{')#This is a set of opening parenthesis
	matches = set([('(',')'),('[',']'),('{','}')])

	stack = []#Making use of the Python list as a stack

	for paren in s:#scan the string from left to right
		if paren in opening:#if paren is a opening parenthesis, then push it to the stack
			stack.append(paren)

		else:#if paren is not a opening parenthesis, then it is obviously a closing parenthesis
			if len(stack) == 0:
				return False

			last_open = stack.pop()

			if (last_open,paren) not in matches:
				return False

	return len(stack) == 0


if __name__ == '__main__':
	my_string = '{()}'
	print(balance_check(my_string))
	my_string_2 = '[]{}([{}])'
	print(balance_check(my_string_2))
	my_string_3 = '{}[}]'
	print(balance_check(my_string_3))