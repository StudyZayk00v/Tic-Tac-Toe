
text = input()
right_dictionary = []
words = text.split()

for word in words:
    if word.casefold().startswith(('https://', 'http://', 'www.')):
        right_dictionary.append(word)

print('\n'.join(right_dictionary))
