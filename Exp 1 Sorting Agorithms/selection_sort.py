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


def selection_sort(arr):
    """Selection Sort function"""
    size = len(arr)
    for i in range(size):
        min_idx = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main():
    # Creating the array
    size = int(input("Enter the size of the array: "))
    
    # Insert the elements in the array
    arr = insert_array_elements(size)
    
    # Display the created array
    print("\nYour array: ", end="")
    display_array(arr)
    
    # Selection Sort the array and then display it
    selection_sort(arr)
    print("\nSelection Sorted array: ", end="")
    display_array(arr)


if __name__ == "__main__":
    main()
