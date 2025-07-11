class ListNode:
    def __init__(self, val):
        self.val= val
        self.next= None

class LinkedList:
    def __init__(self, head, tail):
        self.head= head
        self.tail= tail


    def insert_at_end(self, val):
        # create a new node
        new_node= ListNode(val)
        if self.head is None: # in case the list is empty, make new_node both the head and the tail of the list
            self.head= new_node
            self.tail= new_node
        else:
            # insert the node at the end
            self.tail.next= new_node
            self.tail= new_node
        
    def delete(self,val):
        # if the list is empty, just inform the user of that
        if self.head is None:
            print("The list is already empty.")
            return
        # if the node to delete is the head node
        if self.head.val == val:
            self.head= self.head.next # make the node after the head node, the new head of the list
            if self.head is None: # if the list is now empty, reset tail to None
                self.tail =None
            return
        else:
            # traverse the list to find the node to delete
            current= self.head
            while current:
                if current.next.val == val:
                    # if the node to delete is found, update the pointers
                    current.next= current.next.next
                    if current.next is None:
                        self.tail = current
                    print(f"The node with the value '{val}' got deleted.")
                    return
                current= current.next

    def list_visualizer(self):
        current= self.head
        while current:
            # for the last node in the list, print None as its next memory address
            if current == self.tail:
                print(f"{id(current)}, {current.val}, None")
            else:
                # otherwise print the address of the next node
                print(f" {id(current)}, {current.val}, {id(current.next)}")
            current= current.next


if __name__ == "__main__":
    # Create list and insert elements
    linked_list = LinkedList(None, None)
    linked_list.insert_at_end("apple")
    linked_list.insert_at_end("banana")
    linked_list.insert_at_end("cherry")

    # Visualize
    linked_list.list_visualizer()

    # Delete an element and visualize
    linked_list.delete("banana")
    linked_list.list_visualizer()

    # Delete all elements and visualize
    linked_list.delete("cherry")
    linked_list.delete("apple")
    linked_list.list_visualizer()