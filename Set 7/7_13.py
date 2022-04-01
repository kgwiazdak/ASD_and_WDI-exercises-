class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def delete(pointer):
    while pointer!=None and pointer.next!=None:
        if pointer.value>pointer.next.value:
            pointer.next=pointer.next.next
        pointer=pointer.next


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
    from random import randint
    for i in range(11, 50, 4):
        first.next = Node(randint(1,25))
        first=first.next

    printf(l1)
    delete(l1)
    printf(l1)