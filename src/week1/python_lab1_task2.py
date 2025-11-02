"""
Task 2 – Greeting Function with String Manipulation
--------------------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces with .strip()
- capitalizes the first letter with .capitalize()
- returns "Hello, <Name>! Welcome to Python!"
Ask user for their name and print result.
"""

def greet_user(name):
    name_cleaned = name.strip()
    name_capital = name_cleaned.capitalize()
    return "Hello, " + name_capital + "! welcome to Python!"

if __name__ == "__main__":
    print("Welcome to the Greeter!")
    user_name = input("Please tell me yor full name: ")

    greeting_message = greet_user(user_name)

    print(greeting_message)
