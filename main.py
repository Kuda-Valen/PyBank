import json as js

accounts = []
user_database = []

class User: 
    def __init__(self, name, surname, balance, acc_type, acc_no):
        self.name = name
        self.surname = surname
        self.balance = balance 
        self.acc_type = acc_type
        self.acc_no = acc_no

    




    def add_user():
        print("\n<-- Add new user -->\n")
        name = input("What is user's Name: ")
        surname = input("What is user's Surname: ")
        acc_type = input("User's account preference (A. Savings or B.Checking): ").lower()
        balance = 0

        check_acc_no()

    def to_dict(self):
        return {
            "name" : self.name, 
            "surname" : self.surname,
            "acc_type" : self.acc_type,
            "balance" : self.balance
        }

def check_acc_no(self):
        if not acc_no in accounts:
            acc_no = 100000
        else:
            acc_no = accounts[-1] + 1

        accounts.append(acc_no)

def save(self):
    user_database.append(User(self.name, self.surname, self.acc_type, self.balance))
    
def save_users(users, filename="users.json"):
    dict_list = [user.to_dict() for user in users]

    with open(filename, "w") as file:
        js.dump(dict_list, file, indent=4)

save_users(user_database)


if __name__ == "__main__":
    User = User()

    while True:
        print("\n<== PyBank Banking System ==>\n")