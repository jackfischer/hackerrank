
class Trie:
    def __init__(self):
        self.totalbelow = 0
        self.children = {}

    def add(self, word: str):
        temp = self
        for c in word:
            if c not in temp.children:
                temp.children[c] = Trie()
            temp.totalbelow += 1
            temp = temp.children[c]
        #temp.totalbelow -= 1 #doesnt matter

    
    def find(self, word: str):
        temp = self
        for c in word:
            if c not in temp.children:
                return 0
            temp = temp.children[c]
        return temp.totalbelow
    

n = int(input())

root = Trie()

for _ in range(n):
    operation, word = input().split()
    if operation == "add":
        root.add(word)
    else:
        print(root.find(word))
    
    
    