#The dictionary Death Troopr stores the colour and Force point value

deathtrooper = { "colour" : "Black", "Force Points" : 5 }

#The two print statements access and display the information
print(deathtrooper["colour"])
print(deathtrooper["Force Points"])

print("\n")
#adding a new key-value

deathtrooper = {"color": "black", "force points": 15}
print(deathtrooper)

deathtrooper["x-position"] = 0
deathtrooper["y-position"] = 25

print("\n")
print(deathtrooper)

print("\n")

#new table for adding to an empty dictionary

aliens = {}

aliens["color"] = "black"
aliens["force points"] = 15
print(aliens)


print("\n")
#modifying values in dictionary

deathTrooper = { "colour" : "Black" }

print("The Death Trooper is wearing " + deathTrooper["colour"] + " colour armour.")

deathTrooper = { "colour" : "Red"}

print("The modified Death Trooper is wearing " + deathTrooper["colour"] + " colour armour.")

print("\n")

deathTroopers = {"x-position": 0, "y-position": 25, "speed": "medium"}

print("Original x-position : " + str(deathTroopers["x-position"]))

if deathTroopers["speed"] == "slow":
    x_increment = 1
elif deathTroopers["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

deathTroopers["x-position"] = deathTroopers["x-position"] + x_increment

print("New x-position : " + str(deathTroopers["x-position"]))

print("\n")

deathTrooper = { "Colour" : "Black" , "Force Points" : 15 }
print("Original key/value pairs")
print(deathTrooper)

del deathTrooper["Force Points"]
print("\nDeath Trooper with points key/value pair deleted")
print(deathTrooper)

print("\n")

#using a dictionary with multiple objects

favourite_language = {
  "jen" : "python",
  "sarah" : "c",
  "edward" : "ruby",
  "phil" : "python",
}

print("Sarah's favourite language is " +
  favourite_language["sarah"].title() +
  ".")

print("\n")

#using get() in a dicionary

deathTrooper = {'Colour': 'Black', 'Speed': 'slow'}

pointValue = deathTrooper.get("Force Points", "No Force Point value assigned")
print(pointValue)

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")












#Challenge 1 : person
#Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live.
#You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

#challenge 2 : favourite numbers
#Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary.
#Think of a favorite number for each person, and store each as a value in your dictionary.
#Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program

#challenge 3 : glossary
#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# - Think of five programming words you’ve learned about in the previous chapters.
#   Use these words as the keys in your glossary, and store their meanings as values.

# - Print each word and its meaning as neatly formatted output.
#   You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line.
#   Use the newline character (\n) to insert a blank line between each word-meaning pair in your output

person = {"first_name" : "Lennon",
          "last_name" : "taylor",
          "age" : 17,
          "city/location" : "Portsmouth"
          }
print(person)

fav_number = {"lennon" : 7,
              "jack" : 4,
              "james" : 19,
              "dylan" : 21,
              "samual" : 8
              }

if "lennon" in fav_number:
    print("lennons favourite number is 7")
print(fav_number)

