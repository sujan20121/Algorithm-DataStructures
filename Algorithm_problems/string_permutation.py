"""
A Python code to generate permuations of a given string using a recursive approach
"""
#A random comment
def permu_generator(input_string):
  if len(input_string) == 1:
    return [input_string]

  else:
    letters_except_last = input_string[:len(input_string)-1]
    last_letter = input_string[-1]

    permu_of_letters_except_last = permu_generator(letters_except_last)#get all the permutations of the input string except the last letter

    permutations = []

    for perms in permu_of_letters_except_last:
      for i in range(len(perms)):
        permutations.append(perms[:i] + last_letter + perms[i:])

    return permutations
