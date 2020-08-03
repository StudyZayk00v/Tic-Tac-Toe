scores = input().split()
incorrect = 0
correct = 0
# put your python code here
for answer in scores:
    if answer == 'I':
        incorrect += 1
        if incorrect == 3:
            print('Game over')
            break
    else:
        correct += 1
else:
    print('You won')
print(correct)
