
def twoSum(nums, target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return []


def twoSum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):  # avoid repeating and comparing the same index
            if nums[i] + nums[j] == target:
                return [i, j]
            

def twoSum_brute_force_enumerate(nums, target):
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i + 1:], start=i + 1):
            if num1 + num2 == target:
                return [i, j]

if __name__ == '__main__':

    # hashmap
    nums = [2,7,11,15]
    target = 13
    print("NElements for target sum:", twoSum(nums, target))

    # Brute Force
    nums = [2,7,11,15]
    target = 13
    print("Elements for target sum:", twoSum_brute_force(nums, target))

      # Brute Force
    nums = [2,7,11,15]
    target = 13
    print("Elements for target sum:", twoSum_brute_force_enumerate(nums, target))


# 1. Two Sum


# Support Document
    Video = 'https://www.youtube.com/watch?v=2ObVc2QvZG0'

# Brute Force           Hashmap

# Temporal O(n^2)       O(n)
# Spatial  O(1)         O(n)

# Logarítmica           Linear, More memory required, depending on the number of elements
# N*N on Array
