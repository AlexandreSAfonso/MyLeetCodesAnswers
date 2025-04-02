
def maxSubArrayTwoPointer(nums):
    i = 0  # Initial Pointer Beguin of windows
    j = 0  # Final Pointer End of windows
    n = len(nums)  # Lenght
    ans = float('-inf')  # minor answer 
    cur = 0  # Actual Comulative Sum
    
    while j < n:
        cur += nums[j]  # Actual Sum Add
        ans = max(ans, cur)  # Actualiza actual bigger sum 
        
        while cur < 0:  # On negative sum
            cur -= nums[i]  # decrement beguin windows
            i += 1  # Move pointer
        
        j += 1  # Move pointer
    
    return ans  

def maxSubArrayFast(nums):
    max_row = -9999999999
    cur_row = -9999999999
    for i in nums:
        if cur_row > max_row:
            max_row = cur_row
        if cur_row < 0:
            cur_row = 0
        cur_row += i
    if cur_row > max_row:
            max_row = cur_row
    return max_row


def maxSubArray(nums):    
    maxSum = float('-inf')
    currentSum = 0
    
    for num in nums:
        currentSum += num
        
        if currentSum > maxSum:
            maxSum = currentSum
        
        if currentSum < 0:
            currentSum = 0
    
    return maxSum

if __name__ == '__main__':

    nums = [5,4,-1,7,8] # return 23
    #nums = [-2,1,-3,4,-1,2,1,-5,4] # return 6


    
    #print("Max Continues SUM:",maxSubArrayTwoPointer(nums))
    print("Max Continues SUM:",maxSubArrayFast(nums))
    print("Max Continues SUM:",maxSubArray(nums))
    

# 53. Maximum Subarray