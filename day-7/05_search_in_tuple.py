nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter number to search: "))

i = 0

while i < len(nums):
    if nums[i] == x:
        print("Found at index", i)
        break
    i += 1
else:
    print("Not Found")


#using for loop

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x=25
for i in range (0,len(nums)):
    if nums[i]==x:
        print("found it",i)
        break
    else:
        print("not found")
print("using for loop")
