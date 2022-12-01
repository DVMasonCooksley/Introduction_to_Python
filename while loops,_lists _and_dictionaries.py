# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user : " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print("\n")
print("\n")
print("\n")


# Say you have a list of pets with the value 'cat' repeated several times.
# To remove all instances of that value, you can run a while loop until 'cat' is no longer in the list, as shown here:

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

print("\n")

#Filling a Dictionary with User Input
#You can prompt for as much input as you need in each pass through a while loop.
# Let’s make a polling program in which each pass through the loop prompts for the participant’s name and response.
# We’ll store the data we gather in a dictionary, because we want to connect each response with a particular user:

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
 # Prompt for the person's name and response.
 name = input("\nWhat is your name? ")
 response = input("Which mountain would you like to climb someday? ")

 # Store the response in the dictionary:
 responses[name] = response

 # Find out if anyone else is going to take the poll.
 repeat = input("Would you like to let another person respond? (yes/ no) ")
 if repeat == 'no':
   polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
 print(name + " would like to climb " + response + ".")