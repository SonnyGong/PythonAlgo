from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next != None:
            if head.val == head.next.val:
                head.val = head.next.next.val

        else:
            return head
        self.deleteDuplicates(head.next.next)

if __name__ == '__main__':
    s = Solution()
    print(s.deleteDuplicates(ListNode(1, ListNode(2, ListNode(3)))))