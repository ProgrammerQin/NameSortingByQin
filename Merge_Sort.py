letter_list = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# MergeSort in Python
def mergeSort(name_list):
    n = len(name_list)
    name_list = [" ".join(k.split(" ")[::-1]) for k in name_list]

    if len(name_list) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(name_list)//2
        L = name_list[:r]
        M = name_list[r:]
        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            letter_index = 0

            # if M[j] == ['']:
            #     name_list[k] = L[i]
            #     i = i + 1
            #     k = k + 1
            #     break
            #
            # if L[i] == ['']:
            #     name_list[k] = M[j]
            #     j = j + 1
            #     k = k + 1
            #     break

            while letter_list.index(L[i][letter_index].lower()) == letter_list.index(M[j][letter_index].lower()):
                letter_index = letter_index + 1

                if letter_index == len(L[i]):
                    name_list[k] = L[i]
                    print("Li filled", L[i], name_list)
                    i = i + 1
                    k = k + 1
                    break

                if letter_index == len(M[j]):
                    name_list[k] = M[j]
                    print("Mj filled", M[j], name_list)
                    j = j + 1
                    k = k + 1
                    break

            if letter_list.index(L[i][letter_index].lower()) < letter_list.index(M[j][letter_index].lower()):
                print(L[i], M[j], k, name_list)
                name_list[k] = L[i]
                print("Li Sort", L[i], name_list)
                i = i + 1
                k = k + 1

            else:
                name_list[k] = M[j]
                print("MJ Sort", M[j], name_list)
                j = j + 1
                k = k + 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            name_list[k] = L[i]
            print("LI add", L[i], name_list)
            i += 1
            k += 1

        while j < len(M):
            name_list[k] = M[j]
            print("MJ add", M[j], name_list)
            j += 1
            k += 1
    return name_list



