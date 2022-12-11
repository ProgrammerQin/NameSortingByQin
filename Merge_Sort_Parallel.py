# from Get_name_list import name_list
name_list = [1, 2, 3, 4, 5, 6]
# n = len(name_list)

# letter_list = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# name_list = [" ".join(k.split(" ")[::-1]) for k in name_list]

def merge_sort(a_list):
    length = len(a_list)

# Return immediately if the list has only one element, which is a trivial case for sorting
# Note that this is also the termination condition for the recursion!
    if length <= 1:
        return a_list
    middle_index = length / 2
    print(middle_index)
    left = a_list[0:middle_index]
    right = a_list[middle_index:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

print(merge_sort(name_list))
