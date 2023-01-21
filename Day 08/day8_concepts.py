# # Functions
#
# #Review:
# #Create a function called greet()
# #Write three print statements inside the function.
# #Call greet() function and run your code.
#
# #Function
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
#
# greet()
# #
# # Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
# greet_with_name("Dhaval")
# name - is a parameter
# "Dhaval" - is an argument

#Function with multiple parameters
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}?")

# positional arguments
greet_with("Dhaval","Vadodara")
greet_with("Dev","Ahmedabad")

# keyword arguments
greet_with(name="Meet",location="Mumbai")
greet_with(location="Mumbai",name="Ishan")