
def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num  # Atualiza o candidato
        count += (1 if num == candidate else -1)

    return candidate

if __name__ == '__main__':

    nums = [3,2,3]
    
    #Output: 7, nums = [0,0,1,1,2,3,3,_,_]

    k= majorityElement(nums)
    print("Número majoritário do conjunto:",k)
    #print("Array modificado:", arr) 

# 169. Majority Element