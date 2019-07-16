# Initial commit..
# TO-DO: Complete the selection_sort() function below


def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    print(arr)


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        next_index = i + 1
        for j in range(next_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        print(f'smallest: {arr[smallest_index]}')
        if i != smallest_index:
            # temp = arr[i]
            # arr[i] = arr[smallest_index]
            # arr[smallest_index] = temp
            # print(arr)
            swap(arr, i, smallest_index)

    return arr


selection_arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(selection_sort(selection_arr))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        print(arr)
        for j in range(0, i - 1):
            next_index = j + 1
            if arr[j] > arr[next_index]:
                swap(arr, j, next_index)
    return arr


bubble_sort(selection_arr)
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
