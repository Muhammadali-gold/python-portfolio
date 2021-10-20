from typing import List


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, n in enumerate(nums):
            if target - n in num_to_index:
                return [num_to_index[target - n], i]
            num_to_index[n] = i
        return []


class Solution2(object):
    def addTwoNumbers(self,l1:ListNode,l2:ListNode):
        prev = result=ListNode(None)
        carry=0
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry%10)
            prev = prev.next
            carry//=10

        return result.next


class Solution3(object):
    def theLongestSubstring(self, s: str) -> int:
        last_seen={}
        start=0
        longest=0
        for i,c in enumerate(s):

            if c in last_seen and last_seen[c]>= start:
                start = last_seen[c]+1
            else :
                longest = max(longest,i-start+1)

            last_seen[c]=i
        return longest


#  Main
sol = Solution1()
assert sol.twoSum([1, 2, 4, 5, 5], 10) == [3, 4]
