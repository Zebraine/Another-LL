class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked List is Empty!!")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next

    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node

    def insert_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.next
        if n is None:
            print("Node is not present in Linked List")
        else:
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node

    def insert_before(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data==x:
                break
            n = n.next        
        if n.next is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node    

    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked List is empty!!") 

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        else:
            self.head=self.head.next

    def delete_end(self):
        if self.head is None:
            print("The Linked List is already empty")
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None

    def delete_by_value(self,x):
        if self.head is None:
            print("Can't delete Linked List is empty")
            return
        if x==self.head.data:
            self.head=self.head.next
            return
        n=self.head
        while n.next is not None:
            if x==n.next.data:
                break
            n=n.next
        if n.next is None:
            print("Node is not present!!")
        else:
            n.next=n.next.next

    def reverseLinkedList(self):
        prevPtr = None
        currentPtr = self.head
        while(currentPtr is not None):
            next = currentPtr.next
            currentPtr.next = prevPtr
            prevPtr = currentPtr
            currentPtr = next
        self.head = prevPtr


    def find_index(self, key):
        current = self.head
        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index = index + 1
        return -1
    
    def elemCount(self):
        temp=self.head 
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count


# PyLL=LinkedList()
# PyLL.insert_begin(10)
# PyLL.insert_begin(20)
# PyLL.insert_begin(30)
# PyLL.display()
# print(PyLL.find_index(10))
# print(PyLL.elemCount())
# PyLL.display()