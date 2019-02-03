def i_i_sum(num):
	#base case
	if num == 0:
		return 0

	else:
		modulo = num%10
		num = int(num/10)
		return modulo + i_i_sum(num)


a = 4321
print(i_i_sum(a))
