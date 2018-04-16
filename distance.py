
# coding: utf-8

def similarity(word1,word2):
    lettersCount = 0
    if len(word1) <= len(word2):
        lettersCount = len(word1)
    else:
        lettersCount = len(word2)    
    editDistance = 0    
    for i in range(lettersCount):        
        letterDistance = ord(word1[i]) - ord(word2[i])     
        print word1[i],word2[i],letterDistance
        editDistance += letterDistance
    return editDistance
