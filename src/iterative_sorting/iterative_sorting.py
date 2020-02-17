# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range  (cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True

    while swapped:
        swapped = False
        
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i] 
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swapped = True
  
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return arr

    max_range = range(max(arr) + 1)
    number_occurrences = {}
    running_sum = {}
    count = 0
    result_arr = [None] * len(arr)

    for num in max_range:
        number_occurrences[f"{num}"] = 0

    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"

        number_occurrences[f"{num}"] += 1

    for num in max_range: 
        count += number_occurrences[f"{num}"]
        running_sum[f"{num}"] = count

    for num in arr:
        result_arr[running_sum[f"{num}"]-1] = num
        running_sum[f"{num}"] -= 1

    print(result_arr)
    return result_arr

#Lecture implement insertion_sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]

        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        
        arr[j] = temp

    return arr


