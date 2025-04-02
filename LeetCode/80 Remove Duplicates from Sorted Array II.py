  

def removeDuplicates(nums):
    ## Complexidade Espacial e Temporal 
    # O(1) Solution
    
    lenNuns = len(nums)

    if lenNuns <= 1:
        return len(nums)

    left = 1
    count = 1
    rangeLoops = range(1, lenNuns)
    
    for i in rangeLoops:
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[left] = nums[i]
            left += 1

    nums[:] = nums[:left]
    return left

if __name__ == '__main__':

    nums = [0,0,1,1,1,1,2,3,3]
    
    #Output: 7, nums = [0,0,1,1,2,3,3,_,_]

    k= removeDuplicates(nums)
    print("Número de elementos restantes:",k)
