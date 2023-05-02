import random
import math

class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current.link == None:
        return

    print(current.data[0], '편의점',',','거리 : ',current.data[1],'\n',end='')
    while current.link != start:
        current = current.link
        print(current.data[0], '편의점',',','거리 : ',current.data[1],'\n',end='')
    print()
        
        
memory=[]
head,current,pre = None,None,None

if __name__ == "__main__":
    store = []

    x = []
    y= []
    for _ in range(10):
        x.append(random.randint(1, 100))
    for _ in range(10):
        y.append(random.randint(1, 100))
    for _ in range(10):
        store.append(random.randint(1, 100))

    i=0
    
    while True:
        if i==10 :
            break
        else:
            store[i]=chr(65+i),math.sqrt(x[i]*x[i]+y[i]*y[i])
            i+=1
            
    store.sort(key=lambda x:x[1])
    storeArray = tuple(store)

    node = Node()
    node.data =  storeArray[0]
    head =  node
    node.link = head
    memory.append(node)
    
    for data in storeArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)