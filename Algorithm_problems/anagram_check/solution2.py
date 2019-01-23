def anagram(s1,s2):
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ','').lower()

	if len(s1) != len(s2):
		print('Not anagram')
		return

	count = {}

	for letter in s1:
		if letter in count:
			count[letter]+=1
		else:
			count[letter]=1

	for letter in s2:
		if letter in count:
			count[letter]-=1
		else:
			count[letter]=1

	for k in count:
		if count[k]!=0:
			print('Not anagram')
			return
		else:
			print('Yes anagram')
			return

if __name__ == '__main__':
	s1 = 'abcde'
	s2 = 'abcde'
	anagram(s1,s2)