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


def counting_sort(arr):
    """Counting Sort function"""
    size = len(arr)
    maxval = max(arr)
    
    count = [0] * (maxval + 1)
    for num in arr:
        count[num] += 1
    
    for i in range(1, maxval + 1):
        count[i] += count[i - 1]
    
    sorted_arr = [0] * size
    for i in range(size - 1, -1, -1):
        sorted_arr[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    print("\nCounting Sorted array: ", end="")
    display_array(sorted_arr)


def main():
    # Creating the array
    size = int(input("Enter the size of the array: "))
    
    # Insert the elements in the array
    arr = insert_array_elements(size)
    
    # Display the created array
    print("\nYour array: ", end="")
    display_array(arr)
    
    # Counting Sort the array and then display it
    counting_sort(arr)


if __name__ == "__main__":
    main()
