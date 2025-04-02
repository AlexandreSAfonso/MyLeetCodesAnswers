
def twoSum(nums, target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return []


if __name__ == '__main__':

    nums = [2,7,11,15]
    target = 13

    print("Número de elementos restantes:", twoSum(nums, target))


# 1. Two Sum