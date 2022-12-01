user_0 = {
    'username' : 'askywalker',
    'first' : 'anakin',
    'last' : 'skywalker',
    }

favourite_language = {
  "jen" : "python",
  "sarah" : "c",
  "edward" : "ruby",
  "phil" : "python",
}

for name, language in favourite_language.items():
  print(name.title() +"'s favourite languages is " +
  language.title() + ".")



print("\n")
print("\n")
print("\n")
print("\n")



favourite_language = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

friends = ["phil", "sarah"]
for name in favourite_language.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favourite language is " +
              favourite_language[name].title() + "!")

