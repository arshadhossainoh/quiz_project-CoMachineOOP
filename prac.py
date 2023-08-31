class User:
    active_users = 0
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.school = "ashland university"
        User.active_users += 1

    def __str__(self):
        return f"{self.first} {self.last} is {self.age} years old going to {self.school}"
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th {self.first}"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.first} logged out"


user1 = User('arshad', 'hossain', 35)
user2 = User('kane', 'balam', 34)
# print(user1.is_senior())
# print(user1.birthday())
#print(user2)

print(User.active_users)
print(user1)
print(user1.logout())
print(User.active_users)