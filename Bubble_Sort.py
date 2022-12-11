letter_list = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# This step is to get exchange last name with first name

# Step 1: split each item into a list, around the commas:
# name_list = [k.split(" ") for k in name_list]
# print("Split with a commas", name_list)

# Step 2: reverse the split up list
# name_list = [k.split(" ")[::-1] for k in name_list]
# print("Reverse the split", name_list)

# Step 3; join it back together with a space:
# name_list = [" ".join(k.split(" ")[::-1]) for k in name_list]
# print("After Reverse", name_list)




def bubblesort(name_list):

    n = len(name_list)
# i  the index of the first name in the list
    for i in range(n):
        # j is the index of the rest of names in the list
        for j in range(0, n-i-1):
            # print("the i th name:", i, "the J th letter:", j)

            # k is the number of the letter in the name we are comparing
            k = 0
            while letter_list.index(name_list[i][k].lower()) == letter_list.index(name_list[j][k].lower()):
                k = k + 1
                if k == len(name_list[i]) or len(name_list[j]):
                    name_list[i], name_list[j] = name_list[j], name_list[j]
                    break

            if letter_list.index(name_list[i][k].lower()) > letter_list.index(name_list[j][k].lower()):
                name_list[i], name_list[j] = name_list[i], name_list[j]

            if letter_list.index(name_list[i][k].lower()) < letter_list.index(name_list[j][k].lower()):
                name_list[i], name_list[j] = name_list[j], name_list[i]

    return name_list
