def isStackFull():
    global SIZE,stack,top
    if (top>=SIZE-1):
        return True
    else:
        return False


def isStackEmpty():
    global SIZE,stack,top
    if (top==-1):
        return True
    else:
        return False

def push(data):
    global SIZE,stack,top
    if((isStackFull())):
        print("스택이 꽉찼습니다.")
        return
    top += 1
    stack[top] = data
    

def pop():
    global SIZE,stack,top,s,home
    if(isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    s += 1
    home[s] = stack[top]
    top -= 1

    return home



SIZE = 6
home = [None for _ in range(SIZE)]
stack = ["주황","초록",'파랑','보라','빨강','노랑']
top = -1
s= -1

if __name__ == "__main__":
    
    i=0
    for data in stack:
        push(data)
            
    for data in stack:

        data =pop()
    
    
    
    
    
    print("과자집에 가는길",stack[i],"==>",stack[i+1],"==>",stack[i+2],"==>",stack[i+3],"==>",stack[i+4],"==>",stack[i+5],"-->","과자집")
    print("우리집에 오는길 : ",home[i],"==>",home[i+1],"==>",home[i+2],"==>",home[i+3],"==>",home[i+4],"==>",home[i+5],"-->","우리집")