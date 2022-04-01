class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def add(pointer):
    NewList = Node()
    first = NewList
    prev= pointer
    pointer=pointer.next
    while pointer!=None and pointer.next!=None:
        new = Node(pointer.value+prev.value)
        NewList.next=new
        NewList = NewList.next
        prev=pointer.next
        pointer=pointer.next.next
    return first.next


def printf(linked_list):
    pointer = linked_list
    while pointer.next!=None:
        print(pointer.value, ' -> ', end='')
        pointer=pointer.next
    print(pointer.value)



if __name__ == '__main__':
    from random import randint
    l1 = Node(5)

    first = l1
    for i in range(11, 50, 4):
        first.next = Node(i*3)
        first=first.next

    printf(l1)
    New_List = add(l1)
    printf(New_List)