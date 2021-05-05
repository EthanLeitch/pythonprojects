from random import choice
sentence = input("Input a sentence: ")
print(''.join(choice((str.upper, str.lower))(c) for c in sentence))

