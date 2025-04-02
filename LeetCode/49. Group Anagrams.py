from collections import defaultdict

def groupAnagrams(strs) :
    anagram_map = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    return list(anagram_map.values())


def groupAnagramsFast(strs) :
    dic = dict()
    lst = []
    result = []
    for i in strs:
        st = tuple(sorted(i))
        if st not in dic:
            dic[st] = [i]
        else:
            dic[st] += [i]
    for i in dic:
        result.append(dic[i])
    return result

if __name__ == '__main__':
# Input: 
    strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    print(groupAnagrams(strs))
    print(groupAnagramsFast(strs))

# 49. Group Anagrams