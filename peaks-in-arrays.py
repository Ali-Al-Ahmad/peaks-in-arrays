numbers_array = [1, 3, 2, 5, 4, 6, 5]
list_of_indices = []
length_of_array = len(numbers_array)

def find_peaks(array):
    for i in range(1, length_of_array-1):
        if  array[i] > array[i-1] and array[i] > array[i+1]:
            list_of_indices.append(i)
            
    # printing the index not the value
    print("indices:", list_of_indices)

find_peaks(numbers_array)
