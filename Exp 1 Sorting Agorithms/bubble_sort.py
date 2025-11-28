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


def bubble_sort(arr):
    """Bubble Sort function"""
    size = len(arr)
    for i in range(size):
        no_swap = True
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                no_swap = False
        if no_swap:
            break


def main():
    # Creating the array
    size = int(input("Enter the size of the array: "))
    
    # Insert the elements in the array
    arr = insert_array_elements(size)
    
    # Display the created array
    print("\nYour array: ", end="")
    display_array(arr)
    
    # Bubble Sort the array and then display it
    bubble_sort(arr)
    print("\nBubble Sorted array: ", end="")
    display_array(arr)


if __name__ == "__main__":
    main()
