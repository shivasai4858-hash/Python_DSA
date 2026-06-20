class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))
    

    def remove_duplicates(self):
            values = set()
            previous = None
            current = self.head
            while current:
                if current.value in values:
                    previous.next = current.next
                    self.length -= 1
                else:
                    values.add(current.value)
                    previous = current
                current = current.next


"""            current = self.head
            while current is not None:
                runner = current
                while runner.next is not None:
                    if runner.next.value == current.value:
                        runner.next = runner.next.next
                        self.length -= 1
                    else:
                        runner = runner.next
                current = current.next"""


ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(2)
ll.append(1)
ll.remove_duplicates()
ll.print_list()
