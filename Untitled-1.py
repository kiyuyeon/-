class Node():
    def __init__(self):
        self.data = None
        self.link = None
        

def insertNode_mail(findData, mail) :
	global memory, head, current, pre

	if head.data == findData :      # 첫 번째 노드 삽입
		node = Node()
		node.data = mail
		node.link = head
		head = node
		return

	current = head
	while current.link != None :    # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = mail
			node.link = current
			pre.link = node
			return

	node = Node()                   # 마지막 노드 삽입
	node.data = insertData
	current.link = node




def insertNode(findData, insertData) :
	global memory, head, current, pre

	if head.data == findData :      # 첫 번째 노드 삽입
		node = Node()
		node.data = insertData
		node.link = head
		head = node
		return

	current = head
	while current.link != None :    # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()                   # 마지막 노드 삽입
	node.data = insertData
	current.link = node


def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data,end=' ')
    while current.link != None:
        current = current.link
        print(current.data,end=' ')
    print()


def makeSimpleLinkedList(namePhone):
    global memory,head,current,pre
    printNodes(head)
    
    node = Node()
    node.data = namePhone
    memory.append(node)
    if head == None:
        head = node
        return

    if head.data[0]>namePhone[0]:
        node.link = head
        head = node
        return

    current = head       
    while current.link != None:
        pre = current
        current = current.link
        if current.data[0] > namePhone[0]:
            pre.link = node
            node.link = current
            return
        
    current.link = node    
        
        

memory = [("지민","harry@naver.com")]
select = -1
head, current , pre = None,None,None

if __name__ == "__main__":
    
    while (select != 5):
        
        select = int(input("선택하세요(1:추가,2:삽입,3:삭제,4:수정,5:종료)-->"))
        
        if(select == 1):
            data = input("이름 -->")
            mess = input("메일주소 -->")
            insertNode(findData,data)
            insertNode_mail(findData, mess)
            print(memory)
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
    
    
    
    print(head)
    node = Node()
    node.data = dataArray
    head = node
    memory.append(node)

    

    for data in dataArray :
        makeSimpleLinkedList(data)
        
    printNodes(head)