
def middleOfList(head):
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    #returns middle of linked list 
    return False