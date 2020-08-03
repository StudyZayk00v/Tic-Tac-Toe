text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

limit = int(input())
new_list = []
for sentence in text:
    for word in sentence:
        if len(word) <= limit:
            new_list.append(word)
print(new_list)

# одной строкой
# print([word for sentence in text for word in sentence if len(word) <= limit])
