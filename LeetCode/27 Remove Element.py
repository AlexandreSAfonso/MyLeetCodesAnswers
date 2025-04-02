
def removeElement1(nums, val):
    expectedNums = []
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            expectedNums.append(nums[i]) 
            k += 1

    return k, expectedNums

def removeElement2(nums, val):
    k = 0  # Índice para armazenar os elementos válidos

    for i in range(len(nums)):
        if nums[i] != val:
            # Substitui o elemento atual na posição correta
            nums[k] = nums[i]
            k += 1

    # Reduz a lista para conter apenas os primeiros k elementos
    nums[:] = nums[:k]
    return k

def removeElement4(nums, val):
    expectedNums = []
    n = len(nums)
    e = n-1
    i = 0

    while i < n:
        if nums[i] != val:
            expectedNums.append(nums[i])
            i += 1
        else:
            i += 1
            if nums[e] != val:
                expectedNums.append(nums[e])
                e -=1
                n -=1
            else:
                e -=1
        
    return n

def removeElement(nums, val):
    left = 0  # Ponteiro da esquerda
    right = len(nums) - 1  # Ponteiro da direita

    while left <= right:
        if nums[left] == val:
            # Se encontramos um valor igual a val, movemos para o final
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1  # Reduz o ponteiro da direita
        else:
            # Se não for igual a val, avançamos para o próximo elemento
            left += 1

    # A lista será modificada in-place, e 'left' é o número de elementos válidos
    nums[:] = nums[:left]

    return left
  

if __name__ == '__main__':

    nums = [0,1,2,2,3,0,4,2] # [3,2,2,3]
    val = 2

    k= removeElement(nums, val)
    print("Número de elementos restantes:",k)
    #print("Array modificado:", arr) 

# 27 Remove Element

# 26. Remove Duplicates from Sorted Array
# 203. Remove Linked List Elements
# 283. Move Zeroes