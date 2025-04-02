
def removeDuplicates(nums):
    left = 0  # Ponteiro da esquerda
    leftNew = 0 # Nova posição
    right = len(nums) - 1  # Ponteiro da direita
    val = None
    numOrig=nums

    while left <= right:
        if nums[left] != val:
            # Se não for igual a val, avançamos para o próximo elemento
            nums[leftNew] = nums[left]   
            val = nums[left]   
            left += 1
            leftNew += 1
        else:
            # Se encontramos um valor igual a val, movemos para o final
            left += 1

    nums[:] = nums[:leftNew]
    return left
  

if __name__ == '__main__':

    nums = [0,0,1,1,1,2,2,3,3,4]
    

    k= removeDuplicates(nums)
    print("Número de elementos restantes:",k)
    #print("Array modificado:", arr) 

# 26. Remove Duplicates from Sorted Array
# 203. Remove Linked List Elements
# 283. Move Zeroes