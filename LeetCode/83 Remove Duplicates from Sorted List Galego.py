
def removeDuplicates1(nums):

    
    numOrig=nums.copy()

    left = 0  # Ponteiro da esquerda
    leftNew = 0 # Nova posição
    counter = 0
    right = len(nums) -1  # Ponteiro da direita
    val = None

    while left <= right:
        act = nums[left]
        actnew = nums[leftNew]
        if nums[left] == val:
            while nums[leftNew] == nums[left]:
                if counter < 2:
                    leftNew += 1
                    counter += 1
                left += 1
        else:
            # Se não for igual a val, avançamos para o próximo elemento
            nums[leftNew] = nums[left]   
            val = nums[left] 
            leftNew += 1
            left += 1
            if counter ==2:
                counter = 1
                
                
            

    nums[:] = nums[:leftNew]
    return left
  

def removeDuplicates(nums):
    ## Complexidade Espacial e Temporal 
    ## O(1) Solution
    
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
    #print("Array modificado:", arr) 

