'''
# @Time   :   2024/04/16 23:37:41
# @Author :   ssw
# @File   :   16_merge_two_sorted_arrays.py 
# @Desc   :   https://leetcode.cn/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
'''
import pytest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = m-1, n -1  # 将i1,i2两个指针分别初始化在两个数组的最后一个元素上
        i = len(nums1) - 1  # 指向num1数组的尾部

        # 从后向前遍历数组，比较两个数组的元素，谁大就在i的位置
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[i] = nums1[i1]
                i1 -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1
            i -= 1
        
        # 如果nums2有剩余，说明剩余元素全是比nums1小
        while i2 >= 0:
            # nums1[: i2 + 1] = nums2[: i2 + 1]
            nums1[i] = nums2[i2]
            i2 -= 1
            i -= 1




# ########################## test case ############################
@pytest.fixture
def s():
    return Solution()

def test_merge(s):
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1, 2, 3]
    m = 3
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3]

    nums1 = []
    m = 0
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    assert nums1 == []

    nums1 = [0]
    m = 0
    nums2 = [3]
    n = 1
    s.merge(nums1, m, nums2, n)
    assert nums1 == [3]


