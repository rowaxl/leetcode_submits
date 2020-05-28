import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lists = [l1, l2]
        values = [0, 0]
        for i in range(len(lists)):
            d = 1
            while lists[i] != None:
                value = values[i]
                value += lists[i].val * d
                values[i] = value
                lists[i] = lists[i].next
                d *= 10

        summary = values[0] + values[1]
        
        result = None
        if summary == 0:
            return ListNode(0, None)

        digits = int(math.log10(summary))
        while digits >= 0:
          v = int(summary / (10 ** digits))
          n = ListNode(val=v, next=None)

          if result == None:
            result = n
          else:
            n.next = result
            result = n

          summary -= v * (10 ** digits)
          digits -= 1
            
        return result
