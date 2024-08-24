import numpy as np

class GenerateLists:
    def __init__(self) -> None:
        self.short_sorted = []
        self.short_regular = []
        self.short_reverse = []

        self.middle_sorted = []
        self.middle_regular = []
        self.middle_reverse = []

        self.long_sorted = []
        self.long_regular = []
        self.long_reverse = []

        self.fill_short()
        self.fill_middle()
        self.fill_long()


    def fill_short(self):
        for i in range(0, 100):
            lst = np.random.randint(0, 100, 100)
            lst = list(int(j) for j in lst)
            self.short_regular.append(lst[:])
            lst.sort()
            self.short_sorted.append(lst[:])
            lst.reverse()
            self.short_reverse.append(lst[:])

    @property
    def get_short_sorted(self):
        return self.short_sorted
    
    @property
    def get_regular_sorted(self):
        return self.short_regular
    
    @property
    def get_reverse_sorted(self):
        return self.short_reverse

    def fill_middle(self):
        for i in range(0, 100):
            lst = np.random.randint(0, 1000, 1000)
            lst = list(int(j) for j in lst)
            self.middle_regular.append(lst[:])
            lst.sort()
            self.middle_sorted.append(lst[:])
            lst.reverse()
            self.middle_reverse.append(lst[:])

    @property
    def get_middle_sorted(self):
        return self.middle_sorted
    
    @property
    def get_middle_sorted(self):
        return self.middle_regular
    
    @property
    def get_middle_sorted(self):
        return self.middle_reverse

    def fill_long(self):
        for i in range(0, 100):
            lst = np.random.randint(0, 10000, 10000)
            lst = list(int(j) for j in lst)
            self.long_regular.append(lst[:])
            lst.sort()
            self.long_sorted.append(lst[:])
            lst.reverse()
            self.long_reverse.append(lst[:])

    @property
    def get_long_sorted(self):
        return self.long_sorted
    
    @property
    def get_long_sorted(self):
        return self.long_regular
    
    @property
    def get_long_sorted(self):
        return self.long_reverse


def main():
    a = GenerateLists()
    print(len(a.get_long_sorted[0]))

if __name__ == "__main__":
    main()



