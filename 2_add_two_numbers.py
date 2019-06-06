# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    @staticmethod
    def get_num_str(linked_list):
        num_str = ''
        while True:
            num_str = str(linked_list.val) + num_str
            if linked_list.next:
                linked_list = linked_list.next
            else:
                break
        return num_str

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1_str = self.get_num_str(l1)
        num_2_str = self.get_num_str(l2)

        num = int(num_1_str) + int(num_2_str)
        num_str = str(num)[::-1]

        return num_str


list_1_1 = ListNode(2)
list_1_2 = ListNode(4)
list_1_3 = ListNode(3)
list_1_1.next = list_1_2
list_1_2.next = list_1_3

list_2_1 = ListNode(5)
list_2_2 = ListNode(6)
list_2_3 = ListNode(4)
list_2_1.next = list_2_2
list_2_2.next = list_2_3

sol = Solution()
reply = sol.addTwoNumbers(list_1_1, list_2_1)
print(reply)