#!/usr/bin/python3
class Node:
    data = 0
    next = None

    def __init__(self, data):
        self.data = data


def countNodes(head):
    count = 1
    current = head
    while(current.next is not None):
        count= count + 1
        current = current.next
    return count

head = Node(4)
node1 = Node(2)
node2 = Node(3)
head.next = node1
node1.next = node2

print(countNodes(head))