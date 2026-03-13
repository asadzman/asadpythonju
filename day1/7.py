import os

def walk(dir_path):
    items = os.listdir(dir_path)

    for item in items:
        full_path = os.path.join(dir_path, item)

        if os.path.isdir(full_path):
            walk(full_path)
        else:
            abs_path = os.path.abspath(full_path)
            print(abs_path)

dir_name = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
walk(dir_name)
