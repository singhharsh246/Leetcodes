
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        if l1 and l2:
            if l1.val >= l2.val:
                dummy = ListNode(l2.val)
                head = dummy
                l2 = l2.next
            else:
                dummy = ListNode(l1.val)
                head = dummy
                l1 = l1.next
        else:
            if l1:
                return l1
            else:
                return l2
                
        while l1 and l2:
            if l1.val >= l2.val:
                dummy.next = ListNode(l2.val)
                l2 = l2.next 
                dummy = dummy.next
            else:
                dummy.next = ListNode(l1.val)
                l1 = l1.next
                dummy = dummy.next
        
        else:
            if l1:
                while l1:
                    dummy.next = ListNode(l1.val)
                    l1 = l1.next
                    dummy = dummy.next
            
            else:
                while l2:
                    dummy.next = ListNode(l2.val)
                    l2 = l2.next
                    dummy = dummy.next
        
        return head
