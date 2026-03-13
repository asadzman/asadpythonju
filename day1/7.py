import os

def findfiles(directory):
    for entry in os.listdir(directory):
        path = os.path.join(directory, entry)

        if os.path.isdir(path):
            yield from findfiles(path)   # recursive call
        else:
            yield path


# user input
directory = input("Enter directory path: ")

print("Files found in directory tree:\n")

for file in findfiles(directory):
    print(file)
