class Node:
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class DoublyListList:
    def __init__(self):
        self.start = None
        self.end = None
    
    def insert_at_start(self, node):
        if self.start == None:
            self.start = self.end = node
        else:
            node.next = self.start
            self.start.prev = node
            self.start = node
    
    def insert_at_end(self, node):
        if self.start == None:
            self.start = self.end = node
        else:
            node.prev = self.end
            self.end.next = node
            self.end = node

    def insert_after(self, data, node):
        if self.start == None:
            print(f"Error inserting Node after {data} in an empty list")
        else:
            target_node = self.get_node(data)
            if target_node == -1:
                print(f"Error inserting Node {data} not found.")
            elif target_node.next == None:
                self.insert_at_end(node)
            elif target_node.prev == None:
                self.insert_at_start(node)
            else:
                node.next = target_node.next
                node.next.prev = node
                target_node.next = node
                node.prev = target_node

    def delete_at_start(self):
        start_node = self.start
        if start_node == None:
            print(f"Error deleting Node from an empty list")
        else:
            self.start = start_node.next
            self.start.prev = None
    
    def delete_at_end(self):
        end_node = self.end
        if end_node == None:
            print(f"Error deleting Node from an empty list")
        else:
            self.end = end_node.prev
            self.end.next = None

    def delete_node(self, data):
        start_node = self.start
        if start_node == None:
            print(f"Error deleting Node from an empty list")
        else:
            target_node = self.get_node(data)
            if target_node == -1:
                print(f"Error deleting Node {data} not found.")
            elif target_node.next == None:
                self.delete_at_end()
            elif target_node.prev == None:
                self.delete_at_start()
            else:
                next_node, prev_node = target_node.next, target_node.prev
                next_node.prev = target_node.prev
                prev_node.next = target_node.next

    def display(self):
        current_node = self.start
        while current_node != None:
            print(current_node)
            current_node = current_node.next

    def get_node(self, data):
        current_node = self.start
        while current_node != None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return -1

linked_list = DoublyListList()

linked_list.insert_at_start(Node(10))
linked_list.insert_at_start(Node(20))
linked_list.insert_at_start(Node(30))

linked_list.insert_after(0, Node(98))
linked_list.display()
