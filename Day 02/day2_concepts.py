# Data Types

# String
print("Hello"[0])
print("123"+"456")

# Integer
print(123+456)
var = 123_456_789

# Float
v = 3.14159

# Boolean
variable = True or False

''' TYPE CASTING / TYPE CONVERSION '''

num_char = len(input("What is your Name? "))

# print("Your name has " + num_char + " characters.") this will givw errors because num_char is INT and others are STRINGS.
print(type(num_char))
num_char = str(num_char)
print(type(num_char))
print("Your name has " + num_char + " characters.")

''' MATHEMATICAL OPERATORS '''
print(3 + 5)
print(type(3 + 5))
print(7 - 4)
print(type(7 - 4))
print(3 * 2)
print(type(3 * 2))
print(6 / 3)
print(type(6 / 3))
print(5 ** 2)
print(type(5 ** 2))

'''
PEMDASLR
()
**
* /
+ -
'''
print(3 * 3 + 3 / 3 - 3)
print(3 *(3 + 3) / 3 - 3)


""" ROUND OFF in python """
print(round(8/3,2))
print(8//3)

""" SHORT HAND OPERATORS """
score = 0
score += 1
score *= 2
score -= 1

""" f-STRING """
print(f"your score is {score}")