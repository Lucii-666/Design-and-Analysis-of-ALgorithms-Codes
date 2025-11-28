def insert_sorted_array_elements(size):
    """Function to insert the array elements"""
    print("Enter the elements of the array")
    arr = []
    for i in range(size):
        element = int(input(f"- Element {i}: "))
        if i != 0 and arr[i - 1] > element:
            print("Array should be in a sorted form!")
            break
        arr.append(element)
    return arr


def display_array(arr):
    """Function to display the array"""
    print(" ".join(map(str, arr)))


def binary_search(arr, left, right, target):
    """Function to binary search"""
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, right, target)
    else:
        return binary_search(arr, left, mid - 1, target)


def main():
    # Creating the array
    size = int(input("Enter the size of the array: "))
    
    # Insert the elements in the array
    arr = insert_sorted_array_elements(size)
    
    target = int(input("Enter the element to be searched in the array: "))
    
    # Display the created array
    print("\nYour array: ", end="")
    display_array(arr)
    
    # Binary search the target
    print("Binary Searching ...")
    result = binary_search(arr, 0, size - 1, target)
    print(f"=> Element found at index {result}")


if __name__ == "__main__":
    main()
