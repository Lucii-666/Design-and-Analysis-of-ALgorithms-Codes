# Merge Sort Implementation
def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		L = arr[:mid]
		R = arr[mid:]

		merge_sort(L)
		merge_sort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Quick Sort Implementation
def quick_sort(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)
		quick_sort(arr, low, pi - 1)
		quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
	pivot = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1

# Example usage
if __name__ == "__main__":
	arr1 = [12, 11, 13, 5, 6, 7]
	arr2 = arr1.copy()
	print("Original array:", arr1)

	merge_sort(arr1)
	print("Sorted array with Merge Sort:", arr1)

	quick_sort(arr2, 0, len(arr2) - 1)
	print("Sorted array with Quick Sort:", arr2)
