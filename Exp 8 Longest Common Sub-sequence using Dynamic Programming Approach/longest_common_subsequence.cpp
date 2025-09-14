// Longest Common Subsequence

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int lcs(string &str1, string &str2)
{
    int m = str1.length();
    int n = str2.length();

    vector<vector<int>> l(m + 1, vector<int>(n + 1, 0));

    for (int i = 1; i < m + 1; i++)
    {
        for (int j = 1; j < n + 1; j++)
        {
            if (str1[i - 1] == str2[j - 1])
            {
                l[i][j] = l[i - 1][j - 1] + 1;
            }
            else
            {
                l[i][j] = max(l[i][j - 1], l[i - 1][j]);
            }
        }
    }
    return l[m][n];
}

int main()
{
    string str1, str2;

    cout << "Enter word 1: ";
    cin >> str1;

    cout << "Enter word 2: ";
    cin >> str2;

    cout << "LCS: " << lcs(str1, str2) << endl;
    return 0;
}