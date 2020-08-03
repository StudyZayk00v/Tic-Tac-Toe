minimum = None

while True:
    some = input()
    if some == '.':
        break
    if minimum is None or float(some) < minimum:
        minimum = float(some)
print(minimum)
