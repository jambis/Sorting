# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # Start merging your single lists of one element together into larger, sorted sets
    i = 0
    j = 0

    while i < len(arrA) or j < len(arrB):
        # If arrA no longer has elements then just place
        # arrB into merged_arr
        if i == len(arrA):
            merged_arr[i+j] = arrB[j]
            j += 1

        # If arrB no longer has elements then just place
        # arrA into merged_arr
        elif j == len(arrB):
            merged_arr[i+j] = arrA[i]
            i += 1

        # If element in arrA is greater than element in arrB then
        # place element in arrB in the merged_arr
        elif arrA[i] > arrB[j]:
            merged_arr[i+j] = arrB[j]
            j += 1

        # If element in arrB is greater than element in arrA then
        # place element in arrA in the merged_arr
        else:
            merged_arr[i+j] = arrA[i]
            i += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # While your data set contains more than one item, split it in half
    # Once you have gotten down to a single element, you have also *sorted* that element
    if len(arr) > 1:
        half = len(arr)//2
        arrA = arr[:half]
        arrB = arr[half:]

        return merge(merge_sort(arrA), merge_sort(arrB))
    else:
        return arr


# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
