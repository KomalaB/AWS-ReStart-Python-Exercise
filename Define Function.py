

#!/usr/bin/python3

# ----- function without arguments -----
print("\n\n\n Fucntion without arguments")
def greeting():
    print("-----------------------------")
    print("         Hello World         ")
    print("-----------------------------")

greeting()

# ----- function with arguments -----
print ("\n\n\nCalling Function with arguments")
def sum_two_numbers(num1, num2):
    total = num1 + num2
    print("{} + {} = {}".format(num1, num2, total))

sum_two_numbers(3, 4)

# ----- function with return value -----
print("\n\n\nCalling Functions with return value")
def num_square(num):
    return num * num

my_num = 3
print(num_square(2))
print(num_square(my_num))