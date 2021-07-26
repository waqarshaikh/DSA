class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class CircularLinkedList:
    def __init__(self):
        self.start = None
        self.length = 0
        
    def insert_at_start(self, node):
        if self.start == None:
            self.start = node.next = node
            self.length += 1
        else:
            node.next = self.start
            if self.start.next == self.start:
                self.start.next = node
                self.start = node
            else: 
                current_node = self.start
                while current_node.next != self.start:
                    current_node = current_node.next
                current_node.next = node
                self.start = node

    def insert_at_end(self, node):
        if self.start == None:
            self.start = node.next = node
            self.length += 1
        else:
            node.next = self.start
            if self.start.next == self.start:
                self.start.next = node
            else:
                current_node = self.start
                while current_node.next != self.start:
                    current_node = current_node.next
                current_node.next = node
               
    def insert_after(self, data, node):
        target_node = self.get_node(data)
        if target_node == -1:
            print(f"Error inserting Node {data} not found")
        else:    
            next_node = target_node.next
            target_node.next = node
            node.next = next_node 

    def delete_from_start(self):
        if self.start == None:
            print("Error deleting from an empty list")
        elif self.start.next == self.start:
            self.start = None
        else:
            last_node = self.get_last_node()
            self.start = self.start.next
            last_node.next = self.start

    def delete_from_end(self):
        if self.start == None:
            print("Error deleting from an empty list")
        elif self.start.next == self.start:
            self.start = None
        else:
            current_node = self.start
            while current_node.next.next != self.start:
                current_node = current_node.next
            current_node.next = self.start

    def delete_node(self, data):
        if self.start == None:
            print("Error deleting from an empty list")
        elif self.start.next == self.start:
            self.start = None
        else:
            current_node = self.start
            if current_node.data == data:
                self.delete_from_start()
            else:
                while current_node.next != self.start:
                    if current_node.next.data == data:
                        current_node.next = current_node.next.next
                    current_node = current_node.next

    def display(self):
        current_node = self.start
        if current_node == None:
            print("None")
        else:
            while current_node.next != self.start:
                print(f"{current_node} {current_node.next}")
                current_node = current_node.next
            
            print(f"{current_node} {current_node.next}")
    
    def get_node(self, data):
        current_node = self.start
        while current_node.next != self.start:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return current_node if current_node.data == data else -1

    def get_last_node(self):
        current_node = self.start
        while current_node.next != self.start:
            current_node = current_node.next
        return current_node

linked_list = CircularLinkedList()
linked_list.insert_at_start(Node(1))
linked_list.insert_at_start(Node(2))
linked_list.insert_at_start(Node(3))
linked_list.insert_at_start(Node(4))


linked_list.display()

print(f"Len: {linked_list.length}")
