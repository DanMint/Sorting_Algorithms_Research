def counting_sort(self, k):
    C = [0] * (k + 1)  

    for j in range(len(self.__counting_data)):
        C[self.__counting_data[j]] += 1

    for i in range(1, k + 1):
        C[i] += C[i - 1]

    B = [0] * len(self.__counting_data)
    for j in range(len(self.__counting_data) - 1, -1, -1):
        B[C[self.__counting_data[j]] - 1] = self.__counting_data[j]
        C[self.__counting_data[j]] -= 1

    return B

Z = [4, 2, 2, 8, 3, 3, 1]
k = max(Z) 
sorted_Z = counting_sort(Z, k)
print(sorted_Z)  
