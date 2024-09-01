#include <iostream>
#include <vector>

using namespace std;

void insertionSort(int arr[], const size_t size) {
    for (int i = 1; i < size; i ++) {
        int key = arr[i];
        int j = i - 1;

        while (j > -1 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j -= 1;
        }

        arr[j + 1] = key;
    }
}

int main() {

    int* arr = new int[5];

    arr[0] = 9;
    arr[1] = -1;
    arr[2] = 1;
    arr[3] = 4;
    arr[4] = 0;

    insertionSort(arr, 5);

    for (size_t i = 0; i < 5; i ++) {
        cout << arr[i] << " ";
    }

    delete[] arr;

    return 0;
}
