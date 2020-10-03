class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def append(self,new_data):
        temp=self.head
        new_node=node(new_data)
        if self.head is None:
            new_node=self.head
        while(temp):
            temp=temp.next

        temp.next=new_node

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def findloop(self):
        p1=self.head
        p2=self.head
        while(p2 is not None):
            if(p2.next is None):
                print('Loop not found')
                break
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                print('Loop Found')
                break

if __name__ == "__main__":
    llist=Linkedlist()
    llist.head=node(1)
    second=node(2)
    third=node(3)
    fourth=node(4)
    fifth=node(5)

    llist.head.next=second
    second.next=third
    third.next=fourth
    fourth.next=fifth

    llist.findloop()


        