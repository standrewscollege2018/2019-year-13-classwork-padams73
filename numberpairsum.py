""" this is a solution to the Google interview question on finding whether an ordered list of numbers has a pair
that adds to a given sum. It is an inefficient solution as it requires us to test potentially all pairs
of numbers therefore is of cost n^2. """


def check_sum(number_sum):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            # included a print statement to enable me to check whether the sums were working
            #print(numbers[i], "+", numbers[j], "=",numbers[i]+numbers[j])
            # when we find a pair we escape the for loops by returning True to the main routine
            if numbers[i] + numbers[j] == number_sum:
                return True

numbers = [1, 2, 3, 9]
number_sum_to_check = 8

if check_sum(number_sum_to_check):
    print("Yes")
else:
    print("No")
