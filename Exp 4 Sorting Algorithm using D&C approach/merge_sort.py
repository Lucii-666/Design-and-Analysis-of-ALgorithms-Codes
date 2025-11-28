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


def merge(arr, left, mid, right):
    """Merge function: merges arr[left..mid] and arr[mid+1..right]"""
    s1 = mid - left + 1  # size of left subarray
    s2 = right - mid     # size of right subarray
    
    larr = []
    rarr = []
    
    for i in range(s1):
        larr.append(arr[left + i])
    for i in range(s2):
        rarr.append(arr[mid + 1 + i])
    
    i = 0
    j = 0
    k = left  # k starts at left
    
    while i < s1 and j < s2:
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1
        k += 1
    
    while i < s1:
        arr[k] = larr[i]
        i += 1
        k += 1
    
    while j < s2:
        arr[k] = rarr[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    """Merge Sort function: sorts arr[left..right]"""
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)       # sort left half
        merge_sort(arr, mid + 1, right)  # sort right half
        merge(arr, left, mid, right)     # merge them


def main():
    size = int(input("Enter size of array: "))
    
    arr = insert_array_elements(size)
    
    print("\nYour array: ", end="")
    display_array(arr)
    
    print("\nMerge-sorted array: ", end="")
    merge_sort(arr, 0, size - 1)
    display_array(arr)


if __name__ == "__main__":
    main()
