class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def get_list(lists):
        node_list = []
        for list_ in lists:
            while list_:
                node_list.append(list_.val)
                list_ = list_.next
        return [ListNode(i) for i in sorted(node_list)]

    def mergeKLists(self, lists):
        # create a sorted list of nodes
        sorted_list = self.get_list(lists)
        if not sorted_list:
            return []

        # attach all consecutive nodes to the first one
        node = sorted_list[0]
        for i in range(1, len(sorted_list)):
            node.next = sorted_list[i]
            node = node.next

        # return the first node
        return sorted_list[0]
