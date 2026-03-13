import re

pattern = r"^\d{10}$"

phone = input("Enter phone number: ")

if re.match(pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")
