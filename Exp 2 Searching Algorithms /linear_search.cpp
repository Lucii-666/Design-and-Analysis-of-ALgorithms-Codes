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
    }
}

// Function to display the array
void display_array(int *arr, int size)
{
    for (int i= 0; i < size; i++) cout << arr[i] << " ";
    cout << endl;
}

// function to linear search
int linear_search(int arr[], int size, int target)
{
    for (int i = 0; i < size; i++) if(arr[i] == target) return i;
    return -1;
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

    // Linear search the target
    cout << "Linear Searching ..." << endl;
    cout << "=> Element found at index " << linear_search(arr, size, target) << endl;

    return 0;
}