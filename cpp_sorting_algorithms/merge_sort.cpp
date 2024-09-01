#include <iostream>
#include <vector>

using namespace std;

#include <climits>  

void merge(int A[], size_t p, size_t q, size_t r);

void mergeSort(int *arr, const size_t p, const size_t r) {
    if (p >= r)
        return;

    size_t q = (p + r) / 2;
    mergeSort(arr, p, q);
    mergeSort(arr, q + 1, r);

    merge(arr, p, q, r);
}

void merge(int A[], size_t p, size_t q, size_t r) {
    size_t n1 = q - p + 1;
    size_t n2 = r - q;

    int L[n1 + 1];
    int R[n2 + 1];

    for (size_t i = 0; i < n1; i++)
        L[i] = A[p + i];

    for (size_t i = 0; i < n2; i++)
        R[i] = A[q + 1 + i];

    L[n1] = INT_MAX;
    R[n2] = INT_MAX;

    size_t i = 0;
    size_t j = 0;

    for (size_t k = p; k <= r; k++) {
        if (L[i] <= R[j]) {
            A[k] = L[i];
            i++;
        } else {
            A[k] = R[j];
            j++;
        }
    }
}


int main() {

    int arr[5] = {9, -1, 1, 4, 0};

    mergeSort(arr, 0, 4);

    for (size_t i = 0; i < 5; i ++) {
        cout << arr[i] << " ";
    }

    return 0;
}
