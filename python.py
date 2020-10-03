class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node

    def insertafter(self,prev_node,new_data):
        new_node=node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def append(self,new_data):
        new_node=node(new_data)
        if self.head is None:
            self.head=new_node
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def deletenode(self,key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                return
        while(temp is not None):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if temp == None:
            return
        prev.next=temp.next
        temp=None
    def deletelist(self):
        current=self.head
        while current:
            nxt=current.next
            del current.data
            current=nxt
    
    def reverse(self):
        prev=None
        current=self.head
        while(current):
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        self.head=prev


            

if __name__=='__main__':
    llist=Linkedlist()
    llist.head=node(1)
    second=node(2)
    third=node(3)

    llist.head.next=second;
    second.next=third;
    
    llist.push(0)
    llist.insertafter(second,'kireeti')
    llist.append('sathvika')
    llist.deletenode('kireeti')
    llist.reverse()
    llist.printlist()
