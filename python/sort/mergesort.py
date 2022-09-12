#!/usr/bin/env python3

def mergesort(array):
    if len(array) > 1:
        midpoint = len(array) // 2
        left_array = array[:midpoint]
        right_array = array[midpoint:]
        mergesort(left_array)
        mergesort(right_array)

        # Left and right arrays are copies. Compare and overwrite the original array.
        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        # Copy over excess values
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
print(arr)
mergesort(arr)
print(arr)
