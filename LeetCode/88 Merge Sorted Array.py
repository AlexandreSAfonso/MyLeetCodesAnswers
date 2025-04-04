
# 88_Merge Sorted Array.py
def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    
    positionlast = m + n -1

    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[positionlast] = nums1[m-1]
            m -= 1
        else:
            nums1[positionlast] = nums2[n-1]
            n -= 1
        
        positionlast -= 1
    while n>0:
        nums1[positionlast] = nums2[n -1]
        n -= 1 
        positionlast -= 1

    print(newarr)

if __name__ == '__main__':

    # nums1 = [1,2,3,0,0,0]
    # m = 3
    
    # nums2 = [2,5,6] 
    # n = 3

    nums1 = [0]
    m = 0
    
    nums2 = [1] 
    n = 1

    merge(nums1, m, nums2, n)


# 88 Merge Sorted Array    