for number in range(5):
    print(number)
print("All done")

n = int(input("Enter a number"))
for counter in range(n):
    print(counter+1)
    
my_list = ["Cat", "Dog", "Chicken"]
print(my_list)
# to print out a list more neatly, use a loop
list_len = len(my_list)

for i in range(list_len):
    print(i+1, my_list[i])

# you can also loop directly through a list and pull out each item one at a time    
for item in my_list:
    print(item)
    
    