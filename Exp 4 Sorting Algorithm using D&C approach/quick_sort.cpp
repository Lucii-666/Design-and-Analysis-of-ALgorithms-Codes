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

// Function for partitioning the array
int partition(int arr[], int low, int high)
{
    int pIndex = low;
    int pivot = arr[high];

    for (int i = low; i < high; i++) if (arr[i] < pivot) swap(arr[i],arr[pIndex++]);
    swap(arr[high],arr[pIndex]);
    return pIndex;
    
}

// Function to quick sort
void quick_sort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);
        quick_sort(arr, low, pi-1);
        quick_sort(arr, pi+1, high);
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

    // Quick Sort the array and then display it
    cout << endl << "Quick Sorted array: ";
    quick_sort(arr, 0, size-1);
    display_array(arr, size);

    return 0;
}