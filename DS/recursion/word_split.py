def word_split(phrase, list_of_words, output = None):

	if output is None:
		output = []

	for word in list_of_words:
		#if the phrase starts with the current word, we have a split point
		if phrase.startswith(word):
			output.append(word)

			return word_split(phrase[len(word):],list_of_words,output)

	return output


test_phrase = 'theclownman'
l_w = ['the','ran','man']

print(word_split(test_phrase,l_w))
