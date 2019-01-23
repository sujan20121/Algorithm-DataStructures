def anagram(s1,s2):
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ','').lower()

	if (sorted(s1) == sorted(s2)):
		print(True)
	else:
		print(False)

if __name__ == '__main__':
	s1 = 'abcde'
	s2 = 'edcba'
	anagram(s1,s2)