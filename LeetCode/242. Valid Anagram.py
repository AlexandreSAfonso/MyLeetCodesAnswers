from collections import defaultdict

def isAnagramHash(s, t) -> bool:
    count = defaultdict(int)
    
    # Count the frequency of characters in string s
    for x in s:
        count[x] += 1
    
    # Decrement the frequency of characters in string t
    for x in t:
        count[x] -= 1
    
    # Check if any character has non-zero frequency
    for val in count.values():
        if val != 0:
            return False
    
    return True

def isAnagram(s, t) -> bool:
    count = [0] * 26
    
    # Count the frequency of characters in string s
    for x in s:
        count[ord(x) - ord('a')] += 1
    
    # Decrement the frequency of characters in string t
    for x in t:
        count[ord(x) - ord('a')] -= 1
    
    # Check if any character has non-zero frequency
    for val in count:
        if val != 0:
            return False
    
    return True

def isAnagramFast(s, t) -> bool:
    d = {i: s.count(i) for i in set(s)}
    q = {j: t.count(j) for j in set(t)}
    return (True if len(s) == len(t) and d == q else False)    

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    # s = "rat"
    # t = "car"

    print(isAnagram(s, t))
    print(isAnagramHash(s, t))
    print(isAnagramFast(s, t))

# 242. Valid Anagram