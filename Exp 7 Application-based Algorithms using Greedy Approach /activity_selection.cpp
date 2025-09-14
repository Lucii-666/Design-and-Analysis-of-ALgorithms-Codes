#include <iostream>
using namespace std;

const int MAX = 100;

void activitySelection(int start[], int finish[], int n) {
    // selection sort
    for (int i = 0; i < n - 1; i++) {
        int minPos = i;
        for (int j = i + 1; j < n; j++) {
            if (finish[j] < finish[minPos]) {
                minPos = j;
            }
        }
        // swap finish
        int tf = finish[i]; finish[i] = finish[minPos]; finish[minPos] = tf;
        // swap start
        int ts = start[i]; start[i] = start[minPos]; start[minPos] = ts;
    }

    cout << "\nSelected activities: ";
    int lastFinish = finish[0];
    cout << "1 ";  // first activity

    for (int i = 1; i < n; i++) {
        if (start[i] >= lastFinish) {
            cout << (i + 1) << " ";
            lastFinish = finish[i];
        }
    }
    cout << endl;
}

int main() {
    int n;
    cout << "Enter number of activities: ";
    cin >> n;

    int start[MAX], finish[MAX];
    cout << "Enter start and finish times:\n";
    for (int i = 0; i < n; i++) {
        cout << "Activity " << (i + 1) << ": ";
        cin >> start[i] >> finish[i];
    }

    activitySelection(start, finish, n);

    return 0;
}
