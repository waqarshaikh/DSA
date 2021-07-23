class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.middle = None
        
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
       
    def insert_at_start(self, node):
        if self.start == None:
            self.end = node
        else:
            node.next = self.start
        self.start = node
    
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
        if self.start == self.end:
            self.start = self.end = None
            return
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
    
    def length(self):
        length = 0
        current_node = self.start
        while current_node != None:
            length += 1
            current_node = current_node.next
        return length

linked_list = SinglyLinkedList()

linked_list.insert_at_end(Node(20))
linked_list.insert_at_end(Node(70))
linked_list.insert_at_end(Node(240))
linked_list.insert_at_end(Node(70))
linked_list.display()

print("Length: ", linked_list.length())