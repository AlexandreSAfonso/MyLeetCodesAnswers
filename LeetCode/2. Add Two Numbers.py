class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def addTwoNumbers1(l1, l2):
    dummyHead = ListNode(0)
    tail = dummyHead
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val if l2 is not None else 0

        sum = digit1 + digit2 + carry
        digit = sum % 10
        carry = sum // 10

        newNode = ListNode(digit)
        tail.next = newNode
        tail = tail.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    result = dummyHead.next
    dummyHead.next = None
    return result


if __name__ == '__main__':

    l1 = [2,4,3] # Explanation: 342 + 465 = 807.
    l2 = [5,6,4] # expected return [7,0,8]
    
    print("SUM :",addTwoNumbers(l1, l2))
    
    # PS não consegui testar 

# 2. Add Two Numbers