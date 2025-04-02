
def lengthOfLastWord(s):
    s = s.rstrip()
    count = 0
    
    for i in range(len(s) - 1, -1, -1):
        
        if s[i] == ' ':
            break
        count += 1

    return count
        



if __name__ == '__main__':

    #s = "Hello World" #spected Return 5

    s = "   fly me   to   the moon  " #spected Return 4
    
    print("Número de elementos restantes:",lengthOfLastWord(s))
    

# 58. Length of Last Word