#!/usr/bin/python3
"""summary"""


class MyInt(int):
    """MyInt has == and != operators inverted"""

    def __ne__(self, num2):
        """inverted ne"""
        return int(self) == int(num2)

    def __eq__(self, num2):
        """inverted eq"""
        return int(self) != int(num2)
