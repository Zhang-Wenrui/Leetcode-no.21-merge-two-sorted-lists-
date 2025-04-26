# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nums=[];head=ListNode(0);dummy=head #为了最后return链表的头结点，创建哨兵节点，因为head节点会因为遍历而置于链表尾部
        while list1:
            nums.append(list1.val)
            list1=list1.next
        while list2:
            nums.append(list2.val)
            list2=list2.next
        nums.sort()
        for k in range(len(nums)):
            head.next=ListNode(nums[k])  #给每个指针赋值
            head=head.next   #向右移动指针
        return dummy.next
