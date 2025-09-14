#include <iostream>
#include <vector>
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

// Counting Sort function
void counting_sort(int arr[], int size)
{
    int maxval = 0;
    for (int i = 0; i < size; i++) maxval = max(maxval, arr[i]);

    vector<int> count(maxval + 1, 0);
    for (int i = 0; i < size; i++) count[arr[i]]++;
    for (int i = 1; i <= maxval; i++) count[i] += count[i - 1];

    int sorted[size];
    for (int i = size - 1; i >= 0; i--) {
        sorted[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    cout << endl << "Counting Sorted array: ";
    display_array(sorted,size);
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

    // Counting Sort the array and then display it
    counting_sort(arr, size);

    return 0;
}