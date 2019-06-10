def is_even(check_number):
    """ This function calculates whether a number is even, returning True or False"""
    
    if check_number % 2 == 0:
        return True
    else:
        return False
    
number = int(input()

if is_even(number)==True:
    print("Even")
else:
    print("Odd")
    
