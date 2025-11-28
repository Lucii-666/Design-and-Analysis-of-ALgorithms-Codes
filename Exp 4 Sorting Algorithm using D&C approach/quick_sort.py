def insert_array_elements(size):
    """Function to insert the array elements"""
    print("Enter the elements of the array")
    arr = []
    for i in range(size):
        element = int(input(f"- Element {i + 1}: "))
        arr.append(element)
    return arr


def display_array(arr):
    """Function to display the array"""
    print(" ".join(map(str, arr)))


def partition(arr, low, high):
    """Function for partitioning the array"""
    pIndex = low
    pivot = arr[high]
    
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
    
    arr[high], arr[pIndex] = arr[pIndex], arr[high]
    return pIndex


def quick_sort(arr, low, high):
    """Function to quick sort"""
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def main():
    # Creating the array
    size = int(input("Enter the size of the array: "))
    
    # Insert the elements in the array
    arr = insert_array_elements(size)
    
    # Display the created array
    print("\nYour array: ", end="")
    display_array(arr)
    
    # Quick Sort the array and then display it
    print("\nQuick Sorted array: ", end="")
    quick_sort(arr, 0, size - 1)
    display_array(arr)


if __name__ == "__main__":
    main()
