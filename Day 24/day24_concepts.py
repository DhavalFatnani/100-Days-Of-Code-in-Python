""" FILE OPERATIONS """

# # READING FROM A FILE
# """ 1st Way """
# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()
#
# """ 2nd Way """
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# WRITING TO A FILE
with open("my_file.txt", mode='a') as file:
    file.write("ADDED TEXT.")
