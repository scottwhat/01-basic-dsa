
def middleOfList(head):
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    #returns middle of linked list 
    return slow