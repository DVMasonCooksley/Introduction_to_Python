current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


print("\n")




prompt = "Enter a series of pizza toppings"
prompt += " press 'quit' when you have filled in you're answer"

active = True

while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)
