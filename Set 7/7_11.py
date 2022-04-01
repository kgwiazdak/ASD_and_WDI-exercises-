class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def add(pointer, val):
    first=pointer
    prev = pointer
    pointer=pointer.next
    while pointer!=None:
        if pointer.value==val:
            prev.next=pointer.next
            return first
        prev=pointer
        pointer=pointer.next
    new = Node(val, first)
    return new


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
    l = add(l1, 69)
    printf(l)