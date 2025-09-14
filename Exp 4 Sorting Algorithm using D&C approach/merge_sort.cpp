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
    for (int i = 0; i < size; i++) cout << arr[i] << " ";
    cout << endl;
}

// Merge function: merges arr[left..mid] and arr[mid+1..right]
void merge(int arr[], int left, int mid, int right)
{
    int s1 = mid - left + 1; // size of left subarray
    int s2 = right - mid;    // size of right subarray

    int *larr = new int[s1];
    int *rarr = new int[s2];

    for (int i = 0; i < s1; i++) larr[i] = arr[left + i];
    for (int i = 0; i < s2; i++) rarr[i] = arr[mid + 1 + i];

    int i = 0, j = 0, k = left; // k starts at left
    while (i < s1 && j < s2)
    {
        if (larr[i] <= rarr[j])
        {
            arr[k++] = larr[i++];
        }
        else
        {
            arr[k++] = rarr[j++];
        }
    }
    while (i < s1) arr[k++] = larr[i++];
    while (j < s2) arr[k++] = rarr[j++];

    delete[] larr;
    delete[] rarr;
}

// Merge Sort function: sorts arr[left..right]
void merge_sort(int arr[], int left, int right)
{
    if (left < right)
    {
        int mid = left + (right - left) / 2;
        merge_sort(arr, left, mid);       // sort left half
        merge_sort(arr, mid + 1, right);  // sort right half
        merge(arr, left, mid, right);     // merge them
    }
}

int main()
{
    cout << "Enter size of array: ";
    int size;
    cin >> size;

    int arr[size];
    insert_array_elements(arr, size);

    cout << endl << "Your array: ";
    display_array(arr, size);

    cout << endl << "Merge-sorted array: ";
    merge_sort(arr, 0, size - 1);
    display_array(arr, size);
    
    return 0;
}
