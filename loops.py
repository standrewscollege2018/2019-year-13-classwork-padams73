# use for loops when you are dealing with a set number of iterations
# for loops can take three parameters (starting number, ending number, increase amount)
for i in range(6):
    print(i)

# while loops run so long as a condition is true
# they can be used like for loops, but you need to set the variable and increment it yourself
counter = 1
while counter <=6:
    print(counter)
    counter += 1

# use while loops whenever you want code to keep repeating until a condition is met
# (such as the user entering "stop")
# do NOT use while True loops. Set a boolean variable to True and run the loop as long as it
# remain True. Set it to False when the condition you are after is met.
my_list = []
keep_asking = True
while keep_asking == True:
    name = input("Enter name ")
    if name == "stop":
        keep_asking = False
    else:
        my_list.append(name)
print(my_list)    

    
    