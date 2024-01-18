class sort():
    def __init__(self, ls):
        self.list = ls
        self.length = len(self.list)

    def insertion_sort(self):
        for i in range(1, self.length):
            
            cur = self.list[i]

            idx = self.bin_index_search(self.list[:i], cur)
            
            self.list = self.push(self.list, idx, i)
            
            self.list[idx] = cur
            
            # for j in range(i-1, -1, -1):
            #     if self.list[j] >cur:
            #         self.list[j+1] = self.list[j]
            #         self.list[j] = cur
            #         cur = self.list[j]
        return self.list
    
    ################################################### insertion sort 안쪽 loop binary search 로 구현 실험
    def bin_index_search(self, ls, val):
        start = 0
        end = len(ls)
        while (start < end):
            mid = (start + end) // 2

            if ls[mid] > val:
                end = mid
            elif ls[mid] < val:
                start = mid + 1
            else:
                return mid
        return start
    
    def push(self, ls ,idx, i): # idx : 빈칸 만들 인덱스, i  :sorted 된 경계 인덱스
        if idx >= len(ls):
            print("index out of range when push")
            return 0

        for k in range(i-1, idx-1, -1):
            ls[k+1] = ls[k]
        
        return ls

    #########################################################
    def slice(self):
        self.list = self.list[:3]


    def selection_sort(self):
        for i in range(self.length -1):
            cur = self.list[i]
            for j in range(i+1, self.length):
                if self.list[j] < cur:
                    self.list[i] = self.list[j]
                    self.list[j] = cur
        return self.list


    def merge_sort(self):
        return self.merge_sort_recur(self.list)

    def merge_sort_recur(self, slice_ls):
        if len(slice_ls) == 1:
            return slice_ls
            
        mid = len(slice_ls)//2
        left = self.merge_sort_recur(slice_ls[:mid])
        right  = self.merge_sort_recur(slice_ls[mid:])
        l = 0
        r = 0
        ans = []

        while (l <= len(left)-1) and (r <= len(right)-1):
            if left[l] < right[r]:
                ans.append(left[l])
                l += 1
            else:
                ans.append(right[r])
                r += 1
            
        if l <= len(left)-1:
            ans += left[l:]
        else:
            ans += right[r:]
        return ans
            





def main():
    ls = input("Number array to sort : ")
    ls.split()
    ls = list(map(float, ls))
    ans = sort(ls)
    print("Insertion sort : ", ans.insertion_sort())
    print("Selection sort : ", ans.selection_sort())
    print("Merge sort : ", ans.merge_sort())




if __name__ == '__main__':
    main()