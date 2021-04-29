class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_value={"M":1000, "CM":900, "D":500, "CD": 400,
                       "C":100,"XC":90, "L":50, "XL":40,
                       "X":10, "IX":9, "V":5, "IV":4, "I":1}
        num = 0
        li = ['CM','CD','XC','XL','IX','IV']
        for i in li:
            if i in s:
                num = num + roman_value[i]
                s = s.replace(i,"")
        for i in s:
            num = num + roman_value[i]
        return num
        
