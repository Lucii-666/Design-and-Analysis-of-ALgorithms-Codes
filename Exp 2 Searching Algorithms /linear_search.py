def insert_sorted_array_elements(size):
    """Function to insert the array elements"""
    print("Enter the elements of the array")
    arr = []
    for i in range(size):
        element = int(input(f"- Element {i}: "))
        arr.append(element)
    return arr


def display_array(arr):
    """Function to display the array"""
    print(" ".join(map(str, arr)))


def linear_search(arr, size, target):
    """Function to linear search"""
    for i in range(size):
        if arr[i] == target:
            return i
    return -1


def main():
    # Creating the array
    size = int(input("Enter the size of the array: "))
    
    # Insert the elements in the array
    arr = insert_sorted_array_elements(size)
    
    target = int(input("Enter the element to be searched in the array: "))
    
    # Display the created array
    print("\nYour array: ", end="")
    display_array(arr)
    
    # Linear search the target
    print("Linear Searching ...")
    result = linear_search(arr, size, target)
    print(f"=> Element found at index {result}")


if __name__ == "__main__":
    main()
