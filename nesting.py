#creating a list of dictionaries

alien_0 = { "colour" : "green", "points" : 5 }
alien_1 = { "colour" : "yellow", "points" : 10 }
alien_2 = { "colour" : "red", "points" : 15 }

aliens = [ alien_0, alien_1, alien_2 ]

for alien in aliens:
  print(alien)

print("\n")
print("\n")
print("\n")



# Make an empty list for storing aliens
aliens = []

# Make 30 Green Aliens
for alien_number in range(30):
    new_alien = {"colour": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print("Total Number of Aliens : " + str(len(aliens)))

print("\n")
print("\n")
print("\n")
print("\n")



favourite_language = {
  "jen" : [ "python", "ruby" ],
  "sarah" : [ "c" ],
  "edward" : [ "ruby", "go" ],
  "phil" : [ "python", "haskell" ],
}

for name, languages in favourite_language.items():
  print("\n" + name.title() +"'s favourite languages are: ")
  for language in languages:
    print("\t" + language.title())

print("\n")
print("\n")
print("\n")
print("\n")

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    }
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


