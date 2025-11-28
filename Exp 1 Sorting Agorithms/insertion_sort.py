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


def insertion_sort(arr):
    """Insertion Sort function"""
    size = len(arr)
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j > -1 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main():
    # Creating the array
    size = int(input("Enter the size of the array: "))
    
    # Insert the elements in the array
    arr = insert_array_elements(size)
    
    # Display the created array
    print("\nYour array: ", end="")
    display_array(arr)
    
    # Insertion Sort the array and then display it
    insertion_sort(arr)
    print("\nInsertion Sorted array: ", end="")
    display_array(arr)


if __name__ == "__main__":
    main()
