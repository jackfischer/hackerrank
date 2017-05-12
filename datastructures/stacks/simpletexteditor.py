from collections import namedtuple

op = namedtuple('op', ['op', 'value'])

stack = []
string = ""

Q = int(input())
for _ in range(Q):
    command = input().split()
    if command[0] == "4": #undo
        operation = stack.pop()
        if operation.op == "2": #reappend last k
            string = string + operation.value
        elif operation.op == "1": #remove k length append
            string = string[:-operation.value]
    elif command[0] == "3": #print
        k = int(command[1])
        print(string[k - 1])
    elif command[0] == "2": #delete last k
        k = int(command[1])
        operation = op(command[0], string[-k:])
        stack.append(operation)
        string = string[:-k]
    elif command[0] == "1": #append
        string = string + command[1]
        operation = op(command[0], len(command[1]))
        stack.append(operation)
