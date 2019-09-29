import random
import sys


def bubble_sort(arr):
    """
    Bubble sort simple alogorithm,
    In first iteration largest element is moved to right most index
    For next iteration second largest is moved to last index - 1 position 
    and continue this till the array sorted

    Time complexity for this bubble sort is O(n^2)
    
    """
    is_sorted = False
    while not is_sorted:
        print("array after iteration is:", arr)
        is_sorted = True
        for num in range(1,len(arr)):
            if(arr[num] < arr[num-1]):
                arr[num-1], arr[num] = arr[num], arr[num-1]
                is_sorted = False


array_size = input("Enter number of element: ")

try:
    array_size = int(array_size)
except:
    print("Please enter valid integer")
    sys.exit()

array = list(range(array_size))
random.shuffle(array)
bubble_sort(array)

assert array == list(range(array_size)), "Bubble sort is working"
