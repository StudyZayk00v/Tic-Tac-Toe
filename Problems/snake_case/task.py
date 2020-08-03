start = input()
final = ""
for char in start:
    if char.isupper():
        final += "_" + char.lower()
    else:
        final += char
print(final)
