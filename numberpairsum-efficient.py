""" This program is a more efficient solution to the Google interview problem on finding whether a 
sorted list of numbers has a pair that adds to a given sum. It starts by adding the lowest and the highest
numbers and then moving inwards from either the bottom (if the sum if too low) or downwards from the top
(if the sum if too high). Much more efficient, with a cost of n. 

I have added a function to generate a list of numbers so we can check just how fast it will run with
larger lists. """

import random

def generate_list():
    numbers_list = []
    while len(numbers_list) < 4:
        number = random.randint(1,10)
        numbers_list.append(number)
    numbers_list = sorted(numbers_list)    
    return numbers_list

def check_sum(counter, number_sum):
    """ i and j represent the indices of the list items we are summing. We start with 0 and the last 
    item in the list, then works inwards. Any printing is purely to help us follow what is happening. """
    
    i = 0
    j = len(numbers)-1
    while True:
        counter += 1
        current_sum = numbers[i] + numbers[j]
        # if the sum is too small, move the lower index up one place
        if current_sum < number_sum:
            print(numbers[i], "+", numbers[j])
            i += 1
            # if the sum is too large, move the upper index down one place
        elif current_sum > number_sum:
            print(numbers[i], "+", numbers[j])
            j -= 1
        else:
            print("Success! {} + {} = {}, taking {} tries".format(numbers[i],numbers[j],number_sum,counter))
            return True
        # if we have passed the midpoint then we have checked all pairs so we can stop
        if i >= j:
            print(counter)
            return False

numbers = generate_list()
number_sum_to_check = random.randint(1,11)
counter = 0
print("Sum", number_sum_to_check)
print(numbers)
if check_sum(counter, number_sum_to_check):
    print("Yes")
else:
    print("No")
print(counter)