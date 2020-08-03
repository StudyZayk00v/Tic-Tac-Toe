prime_numbers = []
for number in range(2, 1000):
    if any(number % some == 0 for some in range(2, number)):
        continue
    prime_numbers.append(number)

