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
            lst = np.random.randint(0, 5000, 5000)
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
    def get_short_regular(self):
        return self.short_regular
    
    @property
    def get_short_rsorted(self):
        return self.short_reverse

    def fill_middle(self):
        for i in range(0, 100):
            lst = np.random.randint(0, 50000, 50000)
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
    def get_middle_regular(self):
        return self.middle_regular
    
    @property
    def get_middle_rsorted(self):
        return self.middle_reverse

    def fill_long(self):
        for i in range(0, 100):
            lst = np.random.randint(0, 500000, 500000)
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
    def get_long_regular(self):
        return self.long_regular
    
    @property
    def get_long_rsorted(self):
        return self.long_reverse


def main():
    a = GenerateLists()
    ss = a.get_short_sorted
    sr = a.get_short_regular
    su = a.get_short_rsorted

    print(len(ss[0]))
    print(len(sr[0]))
    print(len(su[0]))

    ms = a.get_middle_sorted
    mr = a.get_middle_regular
    mu = a.get_middle_rsorted

    print(len(ms[0]))
    print(len(mr[0]))
    print(len(mu[0]))

    ls = a.get_long_sorted
    lr = a.get_long_regular
    lu = a.get_long_rsorted

    print(len(ls[0]))
    print(len(lr[0]))
    print(len(lu[0]))

if __name__ == "__main__":
    main()



