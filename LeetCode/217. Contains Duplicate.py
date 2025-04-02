
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def containsDuplicateHash(nums):
    seen = {}
    for num in nums:
        if num in seen and seen[num] >= 1:
            return True
        seen[num] = seen.get(num, 0) + 1
    return False

def containsDuplicateUnic(nums):
    unique = set()
    for num in nums:
        if num in unique:
            return True
        else:
            unique.add(num)
    return False

if __name__ == '__main__':

    nums = [1,1,1,3,3,4,3,2,4,2] # return True

    #nums = [1,2,3,4] # return False
    

    k= containsDuplicate(nums)
    print("Contain Duplicate:",k)

    print("Contain Duplicate:",containsDuplicateHash(nums))

    print("Contain Duplicate:",containsDuplicateUnic(nums))
    

# 217. Contains Duplicate