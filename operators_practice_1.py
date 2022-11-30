n=5

#all of these expressions do the same.

#addition

n = n + 1

n += 1

print(n)

#subtraction

n = n - 5

n -= 5

print(n)

#multiplication

n = n * 9

n *= 9

print(n)

#division

n = n / 5

n /= 5

print(n)

print("\n")
x = 9
y = 2

z = x + y

print(z)

x = 5

x += 3

print(x)

# Set a value for x

x = 5

# Apply a logical test to x

y = x > 3 and x < 10

# Print the Boolean result of the test

print(y)

#membership operators

x = ["Jedi", "Sith"]
print("Sith" in x)
print("Bounty Hunter" in x)

print("Jedi" not in x)
print("Bounty Hunter" not in x)

#identity operators

x = ["Millenium Falcon", "Luke's X-Wing"]
y = ["Millenium Falcon", "Luke's X-Wing"]
z = x

print(x is z)

print(x is y)

print (x == y)

print(x is not z)

print(x is not y)

print(x != y)

