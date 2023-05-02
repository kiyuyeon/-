def isQueueFull():
    global SIZE,queue,front,rear
    if(rear == SIZE-1):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE,queue,front,rear
    if(front == rear):
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE,queue,front,rear
    if(isQueueFull()):
        print("큐가 꽉 찼습니다")
        return
    rear +=1
    queue[rear] = data
    
def deQueue():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    
    return data

def peek():
    global SIZE,queue,front,rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    return queue[front+1]

    
SIZE = int(input("큐 크기를 입력하세요==> "))
queue = [None for _ in range(SIZE)]
front = rear =  -1

if __name__ == "__main__":
    select= input("삽입(I)/추출(E),확인(V),종료(X) 중 하나를 선택 ==>")
    
    while (select !='X'and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력 데이터 ==>")
            enQueue(data)
            print("대기 중 상태 : ",queue)
            
        elif select == 'E' or select == 'e':
            data = deQueue()
            print(data,"님 식당에 들어감")
            for _ in range(SIZE-1):
                queue[_] = queue[_+1]
            
            front -=1
            rear -=1
            
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> : ",data)
            print("큐 상태 : ",queue)
        else:
            print("입력이 잘못됨 : ")
        
        select= input("삽입(I)/추출(E),확인(V),종료(X) 중 하나를 선택 ==>")
    
    print("식당 영업 종료!")