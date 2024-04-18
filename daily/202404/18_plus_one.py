# -*- coding: utf-8 -*-
"""
@Author:     ssw
@File:       18_plus_one.py
@CreateTime: 2024/4/18
@Change Activity: 2024/4/18
@Desc: https://leetcode.cn/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List

import pytest


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # list->str->int->str->list
        return [int(i) for i in str(int(''.join([str(j) for j in digits])) + 1)]

    def plusOne2(self, digits: List[int]) -> List[int]:
        # 从后往前依次判断末尾是否为9， 如果是9，则将末尾元素置为0，并将0添加到tmp_list中，
        # 直到末尾元素不是9，将末尾元素加1，并将tmp_list添加到末尾，返回digits+tmp_list
        tmp_list = []
        while digits and digits[-1] == 9:
            digits.pop()
            tmp_list.append(0)
        if not digits:
            return [1] + tmp_list
        else:
            digits[-1] += 1
            return digits + tmp_list




@pytest.fixture
def s():
    return Solution()


def test_plus_one(s):
    res = s.plusOne([1,2, 3])
    assert res == [1,2,4]

    res = s.plusOne([4,3,2,1])
    assert res == [4,3,2,2]

    res = s.plusOne([9])
    assert res == [1,0]

    res = s.plusOne([0])
    assert res == [1]

@pytest.fixture(params=[
    ([1, 2, 3], [1, 2, 4]),  # 基本测试用例
    ([9], [1, 0]),           # 最后一位是9的情况
    ([9, 9], [1, 0, 0]),     # 最后两位都是9的情况
    ([0], [1]),              # 仅有一位是0的情况
    ([1], [2]),              # 仅有一位的情况
    ([], [1]),               # 数组为空的情况
])
def input_output(request):
    return request.param

def test_plus_one2(s,  input_output):
    input_digits, expected_output = input_output
    assert s.plusOne2(input_digits) == expected_output