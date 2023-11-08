
# class Solution(object):
#     def reverseList(self, head):
#         prev, curr = None, head
#         while curr:
            
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
#         return prev
   
## RECURSIVE
class Solution(object):
    def reverseList(self, head):
        #take the linked list and break it down
        #last node new head 
        #break case
        
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead