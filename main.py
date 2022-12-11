import time
from Get_name_list import name_list
from Bubble_Sort import bubblesort
from Merge_Sort import mergeSort
from Quick_Sort_Name import quicksort

name_list = ["camqwe", "asd", "fasd", "dasd", "hieqwe", "bsdf"]

start = time.time()

# To sort last time alphabetically
name_list = [" ".join(k.split(" ")[::-1]) for k in name_list]

# Compare
# I implement 3 different sequential techniques for name sorting
# name_list = bubblesort(name_list)
name_list = mergeSort(name_list)
# name_list = quicksort(name_list)

# After sorting, flip first name and last name for display
name_list = [" ".join(k.split(" ")[::-1]) for k in name_list]

print("After Sorting:", name_list)

end = time.time()
Executation_time = float(end - start)*1000
print("Name Sorting Time (ms) Is : ", "%.2f" % Executation_time)

# Sorting Result:
# Sequential Bubble Sort: Sorting Time (ms) is :  186248.11
# Sequential Quick Sort: Sorting TIme (ms) is:  127397.48
