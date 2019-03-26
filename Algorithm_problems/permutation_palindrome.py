#Given a word, check if any its permutation is a palindrome.
"""
Brute force approach would be to come up with every single permutation of the 
given word(taking O(n!)) and then check if each of the
permutation is a palindrome(O(n)) leading to a total of O(n!n) time complexity. This is a
very inefficient approach.
A property of every palindrome is that they have zero or one character whose count is Odd.
Eg: Radar has 2 R's and 2 A's, however d  is the only character with a single count.

A Python set can be used to store elements that have odd count.
"""
def permutation_palindrom(word):
    s = set()
    for i in range(len(word)):
        if word[i] in s:
            s.remove(word[i])#if the character is already present, deleting will ensure the count remains even
        else:
            s.add(word[i])
    if len(s)>1:
        return False
    
    return True
    
  
