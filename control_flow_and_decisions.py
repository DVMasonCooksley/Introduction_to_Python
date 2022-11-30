#The following short example shows how if tests let you respond to special situations correctly.

#Return to the list of Empire Transports and imagine and you want to print out the name of each transport.
# They are proper names, so the names of most should be printed in title case.
# However, the value 'AT-AT' should be printed in all uppercase. The following code loops through a list of names and looks for the value 'At-At'.
# Whenever the value is 'At-At', it’s printed in uppercase instead of title case:

# We create an empty list called empireTransport
empireTransport = []

empireTransport.append("death star")
empireTransport.append("imperial star destroyer")
empireTransport.append("tie fighter")
empireTransport.append("imperial shuttle")
empireTransport.append("At-At")
empireTransport.append("speederbike")

for transport in empireTransport:
    if transport == "At-At":
        print(transport.upper())
    else:
        print(transport.title())

#this will post:

  #  Death Star
  #  Imperial Star Destroyer
  #  Tie Fighter
  #  Imperial Shuttle
  #  AT-AT
  #  Speederbike


# checking for inequality

searchedfor_droid = "bb-8"

if searchedfor_droid != "c3po":
    print("these aren't the droids you're looking for")

# testing numerical comparison

height = 150

if height != 180:
  print("Aren't you a little short for a stormtrooper?")





banned_users = ["Maul", "Siduous", "Vader"]

user = "Luke"

if user not in banned_users:
  print(user.title() + ", you can post a response if you wish.")