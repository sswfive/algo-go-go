'''
# @Time   :   2024/04/18 23:13:56
# @Author :   ssw
# @File   :   17_add_binary.py 
# @Desc   :   https://leetcode.cn/problems/add-binary/description/?envType=study-plan-v2&envId=top-interview-150
'''
import pytest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # 内置函数法
        return bin(int(a, 2) + int(b, 2))[2:]

        

@pytest.fixture
def s():
    return Solution()


def test_add_binary(s):

    a, b = "11", "1"
    res = s.addBinary(a, b)
    assert res == "100"

    a, b = "1010", "1011"
    res = s.addBinary(a, b)
    assert res == "10101"






