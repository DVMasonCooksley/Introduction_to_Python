# Modified slightly, the function greet_user() can not only tell the user Hello! but also greet them by name.

def greet_user(username):
    """Display a Greeting."""
    print("Hello " + username.title() + "!")


greet_user("Anakin")

# task from peta

#Challenge 1 : Message

# Write a function called display_message() that prints one sentence telling everyone what you are learning about in this module.
# Call the function, and make sure the message displays correctly.

#Challenge 2 : Favourite Book

# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as One of my favorite books is Alice in Wonderland.
# Call the function, making sure to include a book title as an argument in the function call.


def display_message(message):
    """display a message."""
    print("Hello " + message.title() + ":D")

display_message("I am learning python at the moment and have just hit module 4 of 6, on the python course from peta.")