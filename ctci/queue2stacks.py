class MyQueue(object):
    def __init__(self):
        self.front = list()
        self.back = list()
    
    def peek(self):
        if not self.back:
            while self.front:
                self.back.append(self.front.pop())
        return self.back[-1]
        
        
    def pop(self):
        if not self.back:
            while self.front:
                self.back.append(self.front.pop())
        return self.back.pop()
        
    def put(self, value):
        self.front.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
