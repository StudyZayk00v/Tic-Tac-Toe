dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

sentence = input().split()
for word in dictionary:
    for right_word in sentence:
        if word == right_word:
            sentence.remove(word)
if sentence:
    print("\n".join(sentence))
else:
    print('OK')
