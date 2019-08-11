# generate a large, sorted, list of numbers between 1 and 100

import random
numbers = []
while len(numbers) < 10:
    number = random.randint(1,100)
    numbers.append(number)
numbers = sorted(numbers)
