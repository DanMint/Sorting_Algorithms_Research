#include <iostream>
#include <vector>

using namespace std;

int* NaiveSort(int arr[], const size_t size) {
    int* newArr = new int[size];

    size_t removed = 0;
    size_t currentAppend = 0;

    while (removed <= size) {
        size_t minIndex = 0;

        for (size_t i = 0; i < size; i ++) {
            if (arr[i] == INT_MAX) {
                continue;
            }
            if (arr[i] < arr[minIndex]) {
                minIndex = i;
            }
        }

        newArr[currentAppend] = arr[minIndex];
        currentAppend += 1;
        removed += 1;
        arr[minIndex] = INT_MAX;
    }

    return newArr;
}

int main() {

    int* arr = new int[5];

    arr[0] = 9;
    arr[1] = -1;
    arr[2] = 1;
    arr[3] = 4;
    arr[4] = 0;

    int* arro = NaiveSort(arr, 5);

    for (size_t i = 0; i < 5; i ++) {
        cout << arro[i] << " ";
    }

    delete[] arro;
    delete[] arr;

    return 0;
}
