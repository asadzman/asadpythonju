# Write a simple program which loops over a list of user data (tuples containing a username,
# email and age) and adds each user to a directory if the user is at least 16 years old. You do
# not need to store the age. Write a simple exception hierarchy which defines a different
# exception for each of these error conditions:
# ● the username is not unique
# ● the age is not a positive integer
# ● the user is under 16
# ● the email address is not valid (a simple check for a username, the @ symbol and a
# domain name is sufficient)
# Raise these exceptions in your program where appropriate. Whenever an exception occurs,
# your program should move onto the next set of data in the list. Print a different error
# message for each different kind of exception.
import re


# Base exception
class UserError(Exception):
    pass


class UsernameNotUniqueError(UserError):
    pass


class InvalidAgeError(UserError):
    pass


class UnderAgeError(UserError):
    pass


class InvalidEmailError(UserError):
    pass


directory = {}


def validate_user(username, email, age):
    # username unique check
    if username in directory:
        raise UsernameNotUniqueError("Username already exists.")

    # age must be positive integer
    if not age.isdigit() or int(age) <= 0:
        raise InvalidAgeError("Age must be a positive integer.")

    age = int(age)

    # age restriction
    if age < 16:
        raise UnderAgeError("User must be at least 16 years old.")

    # simple email validation
    if not re.match(r"^[\w]+@[\w]+\.[\w]+$", email):
        raise InvalidEmailError("Email format is invalid.")

    return age


n = int(input("Enter number of users: "))

for _ in range(n):
    try:
        username = input("Enter username: ")
        email = input("Enter email: ")
        age = input("Enter age: ")

        validate_user(username, email, age)

        # store only username and email
        directory[username] = email
        print("User added successfully\n")

    except UsernameNotUniqueError as e:
        print("Error:", e, "\n")

    except InvalidAgeError as e:
        print("Error:", e, "\n")

    except UnderAgeError as e:
        print("Error:", e, "\n")

    except InvalidEmailError as e:
        print("Error:", e, "\n")


print("\nFinal User Directory:")
for username, email in directory.items():
    print(username, "->", email)
