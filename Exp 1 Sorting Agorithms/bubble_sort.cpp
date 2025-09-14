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

// Bubble Sort function
void bubble_sort(int *arr, int size)
{
    bool no_swap = true;
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size - 1 - i; j++)
        {
            if(arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                no_swap = false;
            }
        }
        if(no_swap) break;
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

    // Bubble Sort the array and then display it
    bubble_sort(arr, size);
    cout << endl << "Bubble Sorted array: ";
    display_array(arr, size);

    return 0;
}