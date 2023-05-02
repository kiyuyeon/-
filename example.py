def add_data(friend,talk):
    
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend,talk
    
    
def insert_data(position,friend,talk):    
    if position < 0 or position > len(katok):    
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    katok.append(None)
    kLen = len(katok)
    
    for i in range(kLen-1,position,-1):
        katok[i]= katok[i-1]
        katok[i-1] = None
        
    katok[position] = friend

def correction_data(position,friend):    
    if position < 0 or position > len(katok):    
        print("데이터를 수정할 범위를 벗어났습니다.")
        return
    
    kLen = len(katok)
    
    for i in range(kLen-1,position-1):
        katok[i]= katok[i-1]
        katok[i-1] = None
        
    katok[position] = friend
    
def delete_data(position):
    if position < 0 or position > len(katok):  
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return
          
    kLen = len(katok)
    katok[position] = None
        
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
            
    del(katok[kLen-1])

katok = []
select = -1

if __name__=="__main__":
    
    while (select != 5):
        
        select = int(input("선택하세요(1:추가,2:삽입,3:삭제,4:수정,5:종료)-->"))
        
        if(select == 1):
            data = input("추가할 데이터 -->")
            mess = int(input("채팅횟수 -->"))
            add_data(data, mess)
            katok.sort(key=lambda x:x[1])
            print(katok)
        elif (select == 2):
            pos = int(input("삽입할 위치 -->"))
            data = input("추가할 데이터 -->")
            insert_data(pos, data)
            print(katok)
        elif (select == 3):
            pos = int(input("삭제할 위치 -->"))
            delete_data(pos)
            print(katok)
            
        elif (select == 4):
            pos = int(input("수정할 위치 -->"))
            data = input("수정할 데이터 -->")
            correction_data(pos, data)
            print(katok)
                
        elif (select == 5):
            print(katok)
            exit()
        else :
            print("1~4 중 하나를 입력하세요")
            continue