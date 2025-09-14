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

// Selection Sort function
void selection_sort(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        int min = i;
        for (int j = i + 1; j < size; j++) if(arr[j] < arr[min]) min = j;
        if (min != i) swap(arr[i], arr[min]);
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

    // Selection Sort the array and then display it
    selection_sort(arr, size);
    cout << endl << "Insertion Sorted array: ";
    display_array(arr, size);

    return 0;
}