
def twromanToIntoSum(s):
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    ans = 0
    
    for i in range(len(s)):
        if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
            ans -= m[s[i]]
        else:
            ans += m[s[i]]
    
    return ans


if __name__ == '__main__':

    nums = "MCMXCIV"
    target = 1994

    k= twromanToIntoSum(nums)
    print("Equivalente a:",k)
    #print("Array modificado:", arr) 

# 13. Roman to Integer