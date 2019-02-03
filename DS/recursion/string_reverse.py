def string_reverse(s):

	#base case
	if len(s) <= 1:
		return s
	#recursion
	return string_reverse(s[1:]) + s[0]
	


my_str = 'abcd'
print(string_reverse(my_str))
