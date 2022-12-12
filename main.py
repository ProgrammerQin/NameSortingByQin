import time
from Get_name_list import name_list
from Bubble_Sort import bubblesort
from Quick_Sort_Name import quicksort
from Merge_Sort_Parallel import merge_sort, merge_sort_parallel


if __name__ == "__main__":
    print("Choose 1 out of 4 techniques for sorting name")
    technique = int(input("1-Bubble Sort  2-Quick Sort  3-Merge Sort Sequential  4-Merge Sort Parallel\n"))

# To sort last time alphabetically
    name_list = [" ".join(k.split(" ")[::-1]) for k in name_list]

# Compare
# I implement 4 different sequential techniques for name sorting
    if technique == 1:
        name_list = bubblesort(name_list)
    if technique == 2:
        name_list = quicksort(name_list)
    if technique == 3:
        name_list = merge_sort(name_list)
    if technique == 4:
        name_list = merge_sort_parallel(name_list)

    start = time.time()
# After sorting, flip first name and last name for display
    name_list = [" ".join(k.split(" ")[::-1]) for k in name_list]

# print("After Sorting:", name_list)

    end = time.time()
    Executation_time = float(end - start)*1000
    print("Name Sorting Time (ms) Is : ", "%.2f" % Executation_time)

# Sorting Result:
# Sequential Bubble Sort: Sorting Time (ms) is :  186248.11
# Sequential Quick Sort: Sorting TIme (ms) is:  127397.48
# Sequential Merge Sort: Sorting TIme (ms) is:  8895.89
# Parallel Merge Sort: Sorting Timer (ms) is: 7646.39
