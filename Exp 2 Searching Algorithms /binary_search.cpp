#include <iostream>
using namespace std;


// Function to insert the array elements
void insert_sorted_array_elements(int *arr, int size)
{
    cout << "Enter the elements of the array" << endl;
    for (int i = 0; i < size; i++)
    {
        cout << "- Element " << i << ": ";
        cin >> arr[i];
        if(i != 0 && arr[i - 1] > arr[i]){
            cout << "Array should be in a sorted form!" << endl;
            break;
        }
    }
}

// Function to display the array
void display_array(int *arr, int size)
{
    for (int i= 0; i < size; i++) cout << arr[i] << " ";
    cout << endl;
}

// function to binary search
int binary_search(int arr[], int left, int right, int target)
{
    int mid = left + (right - left) / 2;
    if(arr[mid] == target) return mid;
    else if(arr[mid] < target) return binary_search(arr, mid+1, right, target);
    else return binary_search(arr, left, mid-1, target);
}

int main(){
    // Creating the array
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;

    // Insert the elements in the array
    int arr[size];
    insert_sorted_array_elements(arr, size);

    int target;
    cout << "Enter the element to be searched in the array: ";
    cin >> target;

    // Display the created array
    cout << endl << "Your array: ";
    display_array(arr,size);

    // Binary search the target
    cout << "Binary Searching ..." << endl;
    cout << "=> Element found at index " << binary_search(arr, 0, size, target) << endl;

    return 0;
}