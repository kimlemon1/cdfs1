class Search():
    def __init__(self, ls):
        self.list = ls
        self.length = len(ls)

    def linear_search(self, n):
        for i in range(self.length):
            if self.list[i] == n:
                return i
            
    def binary_search(self,n):
        return self.recur_bin_search(0, self.length, n)
        
        
    def recur_bin_search(self, start, end, n):
        if start >= end:
            return -1

        mid = (start + end) // 2
        if self.list[mid] > n:
            return self.recur_bin_search(start, mid, n)
        elif self.list[mid] < n:
            return self.recur_bin_search(mid+1, end, n)
        else:
            return mid
        
def main():
    ls = [1,3,4,6,9,11,14,15]
    A = Search(ls)
    search_idx = A.binary_search(-3)
    print(search_idx)

if __name__ == '__main__':
    main()