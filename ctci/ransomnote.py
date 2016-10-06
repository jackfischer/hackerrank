def ransom_note(magazine, rasom):
    words = dict()
    
    for word in magazine:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    
    for word in ransom:
        if word in words and words[word] > 0:
            words[word] -= 1
        else:
            return False
        
    return True
        
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
