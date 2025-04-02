
def longestCommonPrefix(strs):
    if not strs:  
        return ""
    
    min_len = min(len(s) for s in strs)
    
    prefix = ""
    for i in range(min_len):
        char_count = {}
        
        for s in strs: # Add actual caracter of all words
            char_count[s[i]] = char_count.get(s[i], 0) + 1
        
        if len(char_count) == 1:  # Check only one car or break on more one.
            prefix += strs[0][i]
        else:
            break
    
    return prefix

def longestCommonPrefixFast(strs):
    minlen = min([len(s) for s in strs]) 
    
    for i in range(minlen):
        initial = strs[0][i]
        for s in strs:
            
            if s[i] != initial:
                return s[:i]


    return strs[0][:minlen]    


def longestCommonPrefixWord(strs):

    word= ""
    for i in range(len(strs[0])):
        char = strs[0][i]  
        
        for s in range(1, len(strs)):
            
            if i >= len(strs[s]) or strs[s][i] != char:
                return word
        word += char
    
    return word

if __name__ == '__main__':

    strs = ["flower","flow","flight"] #expected return "fl"

    print("Número de elementos restantes:", longestCommonPrefix(strs))

# 14. Longest Common Prefix