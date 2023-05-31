# Creating a Class
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0  # All instances will have this default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Creating an Instance
user_1 = User("001", "angela")
print(user_1.id, user_1.name)

user_2 = User("002", "bob")
print(user_2.id, user_2.name)

user_2.follow(user_1)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)