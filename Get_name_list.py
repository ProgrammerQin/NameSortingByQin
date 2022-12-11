# opening the file in read mode

name_file = open("names.txt", "r")
# name_file = open("names_short.txt", "r")

# reading the file
name_data = name_file.read()

# turn txt file to a name list
name_list = name_data.split("\n")

# This step is to remove duplicated names in the list:
name_list = list(dict.fromkeys(name_list))

n = len(name_list)
# print("Length of no duplicates list:", n)


