class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=node(new_data)
        if self.head is not None:
            self.head.prev=new_node
        new_node.next=self.head
        new_node.prev=None
        self.head=new_node

    def insertafter(self,prev_node,new_data):
        new_node=node(new_data)
        if prev_node is None:
            print('the given previous node cannot be Null')
            return
        new_node.next=prev_node.next
        new_node.prev=prev_node
        prev_node.next=new_node
        if (new_node.next is not None):
            new_node.next.prev=new_node
    
    def removenode(self,dele):
        if self.head is None or dele is None:
            return
        
        if self.head == dele:
            self.head=dele.next
            self.head.prev=None
            return


        if dele.next is not None:
            dele.next.prev=dele.prev

        if dele.prev is not None:
            dele.prev.next=dele.next



    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__ == "__main__":
    llist=Linkedlist()
    llist.push(1)
    llist.push(2)
    llist.insertafter(llist.head,'kireeti')
    llist.removenode(llist.head.next)
    llist.printlist()
        