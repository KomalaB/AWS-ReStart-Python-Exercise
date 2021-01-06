#!/usr/bin/python3


# if, if-else, if-elif-else

print("\n\n Using if, if-else, if-elif-else")
num = int(input("Enter a number: "))

# only if
print("\n\nUsing if Condition")
if num > 25:
    print("Hurray! {} is greater than 25".format(num))

# if-else
print("\nUsing if-else Condition")
if num % 2 == 0:
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))

# if-elif-else#
print("\nUsing if-elif-else Condition") 
# any number of elif can be used
if num < 0:
    print("{} is a negative number".format(num))
elif num > 0:
    print("{} is a positive number".format(num))
else:
    print("{} is neither postive nor a negative number".format(num))




#For Conditions
#!/usr/bin/python3

print("\n\nworking with For Conditions ")
numb = int(input("Enter a tables you want to display: "))

for i in range(1, numb+1):
    mul_table = numb * i
    print("{} * {} = {}".format(numb, i, mul_table))


