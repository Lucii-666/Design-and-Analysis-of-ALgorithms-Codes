#include <iostream>
using namespace std;

// Function to insert the array elements
void insert_array_elements(int *arr, int size)
{
    cout << "Enter the elements of the array" << endl;
    for (int i = 0; i < size; i++)
    {
        cout << "- Element " << i + 1 << ": ";
        cin >> arr[i];
    }
}

// Function to display the array
void display_array(int *arr, int size)
{
    for (int i= 0; i < size; i++) cout << arr[i] << " ";
    cout << endl;
}

// Insertion Sort function
void insertion_sort(int *arr, int size)
{
    for (int i = 1; i < size; ++i)
    {
        int key = arr[i];
        int j = i - 1;
        while(j > -1 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}


int main(){
    // Creating the array
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;

    // Insert the elements in the array
    int arr[size];
    insert_array_elements(arr, size);

    // Display the created array
    cout << endl << "Your array: ";
    display_array(arr, size);

    // Insertion Sort the array and then display it
    insertion_sort(arr, size);
    cout << endl << "Insertion Sorted array: ";
    display_array(arr, size);

    return 0;
}


