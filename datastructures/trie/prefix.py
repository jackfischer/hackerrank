
class Trie:
    def __init__(self):
        self.letters = []
        self.children = []
        self.word = False
        
    def process_line(self, line: str) -> bool:
        temp = self
        for c in line:
            if c not in temp.letters:
                temp.children.append(Trie())
                temp.letters.append(c)
            temp = temp.children[temp.letters.index(c)]
            if temp.word:
                return True
            
        temp.word = True
        return len(temp.children) != 0
    

    
n = int(input())
root = Trie()

for _ in range(n):
    line = input()
    if root.process_line(line):
        print("BAD SET")
        print(line)
        break
        
else:
    print("GOOD SET")
        
