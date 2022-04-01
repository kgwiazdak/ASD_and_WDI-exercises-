class Node():
    def __init__(self, value=None, next=None):
        self.value=value
        self.next=next

def if_contains(pointer, val):
    if pointer.value==val:
        return True
    while pointer.next!=None:
        if pointer.value==val:
            return True
            pointer=pointer.next
    return False

def remove(pointer, val):
    first = pointer
    if pointer.value==val:
        return first.next
    prev = None
    while pointer.next!=None:
        prev = pointer
        pointer=pointer.next
        if pointer.value==val:
            prev.next=pointer.next
            return first


def printl(pointer):
    while pointer.next != None:
        print(pointer.value,"-> ",end='')
        pointer = pointer.next
    print(pointer.value, "-> ", end='')
    print("None")


def insert(pointer, val, index):
    i=0
    first = pointer
    if index==0:
        return Node(val, pointer)

    while index-1>i and pointer.next!=None:
        pointer=pointer.next
        i+=1
    if index-1>i:
        print('index out of range ja to mówię')
        return first

    l = Node(val, pointer.next)
    pointer.next=l
    return first




if __name__ == '__main__':
    l = Node(0)
    l = insert(l, 1, 1)
    l = insert(l, 2, 2)
    #l = remove(l, 0)
    l = insert(l, 3, 3)
    printl(l)