from random import randint

# name_list = [1123, 10, 34, 514, 25, 621]
# name_list = ["m", "n", "f", "g", "i", "l"]
# name_list = ["mqwe", "nasd", "fasd", "bgasd", "aieqwe", "lsdf"]

letter_list = ["", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]
    print(pivot)
    for item in array:
        # Elements that are smaller than the `pivot` go to the `low` list
        # Elements that are larger than `pivot` go to the `high` list
        # Elements that are equal to `pivot` go to the `same` list.

        # k is the number of the letter in the name we are comparing
        k = 0
        print("item", item, "Pivot", pivot, "Array", array)

        while letter_list.index(item[k].lower()) == letter_list.index(pivot[k].lower()):
            k = k + 1
            if k == len(item)-1 or len(pivot)-1:
                same.append(item)
                break

        if letter_list.index(item[k].lower()) > letter_list.index(pivot[k].lower()):
            high.append(item)
            print("1")

        if letter_list.index(item[k].lower()) < letter_list.index(pivot[k].lower()):
            low.append(item)
            print("2")


#        if item < pivot:
#            low.append(item)
#            print("low", low)
#        elif item == pivot:
#            same.append(item)
#            print("same", same)
#        elif item > pivot:
#            high.append(item)
#            print("high", high)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

