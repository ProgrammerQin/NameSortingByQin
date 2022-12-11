from random import randint

name_list = [1123, 10, 34, 514, 25, 621]
# name_list = ["m", "n", "f", "g", "i", "l"]


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
        if item < pivot:
            low.append(item)
            print("low", low)
        elif item == pivot:
            same.append(item)
            print("same", same)
        elif item > pivot:
            high.append(item)
            print("high", high)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)


quicksort(name_list)
print(quicksort(name_list))
