"this function finds the peaks in a list where a peak is a number greater than both neighbors"

numbers_array = [1, 3, 2, 5, 4, 6, 5]
list_of_indices = []
LENGTH_OF_ARRAY = len(numbers_array)

def _find_peaks(array):
    for i in range(1, LENGTH_OF_ARRAY-1):
        if  array[i] > array[i-1] and array[i] > array[i+1]:
            print("number:",numbers_array[i])
            list_of_indices.append(i)

    # printing the index not the value
    print("indices:", list_of_indices)

_find_peaks(numbers_array)
