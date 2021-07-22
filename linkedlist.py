class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class SingleLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.middle = None
        self.length = 0

    def insert_after(self, new_node, data):
        node = self.get_node(data)
        new_node.next = node.next
        node.next = new_node

    def insert_at_end(self, node):
        if self.start == None:
            self.start = node
        else:
            self.end.next = node
        self.end = node
        self.length += 1
    
    def insert_at_start(self, node):
        if self.start == None:
            self.end = node
        else:
            node.next = self.start
        self.start = node
        self.length += 1

    def display(self):
        node = self.start
        while node != None:
            print(node, end=' ')
            node = node.next

    def delete_from_start(self):
        start_node = self.start
        self.start = start_node.next
        del start_node

    def delete_from_end(self):
        node = self.start
        end_node = self.end
        while node != None:
            if node.next.next == None:           
                node.next = None
                self.end = node
                del end_node
            node = node.next

    def delete_at(self, data):
        node = self.start
        while node != None:
            print(node.next.data == data)
            if node.next.data == data:
                target_node = node.next
                node.next = node.next.next
                del target_node
                return
            node = node.next

    def get_node(self, data):
        node = self.start
        while node != None:
            if node.data == data:
                return node
            node = node.next

linked_list = SingleLinkedList()

linked_list.insert_at_end(Node(20))
linked_list.insert_at_end(Node(30))
linked_list.insert_after(Node(10), 20)

linked_list.display()


