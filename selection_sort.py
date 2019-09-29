
import random
import sys

def selection_sort(array):
	"""
	Selection sort is also a simple sorting algorithm
	Here first we fix a index point and compare the all the elemet
	such that after complete iteration smallest elemet in will be in index point
	then index point will be increment by one then continue iteration till the array 
	is in correct order

	Time complexity for this selection sort is O(n^2)

	"""
	index = 0
	while index < len(array):
		for num in range(index, len(array)):
			if array[index] > array[num]:
				array[index], array[num] = array[num], array[index]
		print("Array after iteration", array)
		index += 1


array_size = input("Enter number of element: ")

try:
    array_size = int(array_size)
except:
    print("Please enter valid integer")
    sys.exit()

array = list(range(array_size))
random.shuffle(array)
selection_sort(array)


assert array == list(range(array_size)), "Selection sort is not working"
