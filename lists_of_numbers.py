#Turning the results from a range into a list

numbers = range(1,50)

print(numbers)
print("\n")

#Range of 50 from 0 to 50 in 2

numbers_1 = (range(0,50))
even_numbers = list(range(0,50,2))

print(numbers_1)
print(even_numbers)

#Square numbers

print("\n")

squares = []

for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

#minimum, maximum and sum

print("\n")

digits = [1,2,3,4,5,6,7,8,9,0]

print("The minimum value is " + str(min(digits)))
print("The maximum value is " + str(max(digits)))
print("The sum of all values is " + str(sum(digits)))

#List comprehension

print("\n")

squares_1 = [value ** 2 for value in range(1,11)]
print(squares_1)

#trying it out on my own, WISH ME LUCK

print("\n")

num = list(range(1,21))
print(num)
print("\n")
print("This is a list of all the odd numbers between 1 and 20")
print(list(range(1,20,2)))

for valu in range(1,1001):
    print(valu)

for val in range(1,10001):
    print(val)
print("\nThis is a list of 3 up to 30")

print(list(range(3,33,3)))
