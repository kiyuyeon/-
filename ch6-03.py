# def isStackFull():
#     global SIZE,stack,top
#     if (top>=SIZE-1):
#         return True
#     else:
#         return False

def push(data):
    global SIZE,stack,top
    if((top>=SIZE-1)):
        print("스택이 꽉찼습니다.")
        return
    top += 1
    stack[top] = data

def pop(data):
    global SIZE,stack,top
    if(top==-1):
        print("스택이 비었습니다.")
        return None
    
    data = stack[pop]
    stack[top] = None
    top -=1
    return data


# def isStackEmpty():
#     global SIZE,stack,top
#     if(top==-1):
#         return True
#     else :
#         return False

SIZE = 5
top = 0
stack = ["커피",None,None,None,None]

# print("스택이 꽉 찼는지 여부 ==>",isStackFull())
# push("환타")
print(stack)
# push("게토레이")
# print(isStackEmpty())

