#Using a while loop, print all elements of the following list:
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

# for loop 

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in range(0,len(numbers)):
    print(numbers[i])
print("using for loop")