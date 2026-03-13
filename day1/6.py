class USER_DATA:
    def __init__(self, list_data):
        self.list = list_data
        self.MIN_AGE = 16
        self.dict = []
        self.user_names = []

    def is_valid(self, name, email):
        return email.endswith(".com") and "@" in email and name in email

    def add_users(self):
        idx = 1
        for user in self.list:
            errorRaise = False
            name = user[0]
            email = user[1]
            age = user[2]

            try:
                if name in self.user_names:
                    errorRaise = True
                    raise ValueError("user name not unique !")
            except ValueError as e:
                print(f"For user {idx} : {e}")

            try:
                if age < 0:
                    errorRaise = True
                    raise ValueError("age is not positive ")
            except ValueError as e:
                print(f"For user {idx} : {e}")

            try:
                if not name or not self.is_valid(name, email):
                    errorRaise = True
                    raise ValueError("email not valid")
            except ValueError as e:
                print(f"For user {idx} : {e}")

            if not errorRaise:
                if age < self.MIN_AGE:
                    self.dict.append({"name": name, "email": email})
                else:
                    self.dict.append({"name": name, "email": email, "age": age})
            
            self.user_names.append(name)
            idx += 1

    def print_users(self):
        for d in self.dict:
            name = d.get("name")
            email = d.get("email")
            age = d.get("age")

            if name:
                print(name, end="\t")
            if email:
                print(email, end="\t")
            if age:
                print(age, end="\t")
            print()

test_list = [
    ["alice", "alice@test.com", 25],
    ["bob", "bob@mail.com", 12],
    ["alice", "alice2@test.com", 30],
    ["charlie", "wrong-email", 20],
    ["dave", "dave@test.com", -1]
]

user_data = USER_DATA(test_list)
user_data.add_users()
user_data.print_users()