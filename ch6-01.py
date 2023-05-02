stack = [None,None,None,None]
top = -1

top += 1
stack[top] = "커피"
top += 1
stack[top] = "녹차"
top += 1
stack[top] = "꿀물"

for i in range(len(stack)-1,-1,-1):
    print(stack[i])
