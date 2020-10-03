"""
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3

"""

"""
IV -> IIII
IX -> VIIII
XL -> XXXX
XC -> LXXXX
CD -> CCCC
CM -> DCCCC
"""
class Solution:
    @staticmethod
    def romanToInt(s):
        
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        #replacing the values to single roman letters
        s=s.replace('IV','IIII').replace('IX','VIIII')
        s=s.replace('XL','XXXX').replace('XC','LXXXX')
        s=s.replace('CD','CCCC').replace("CM","DCCCC")
        
        result=0
        for ch in s:
            result+=roman_dict[ch]
        return result
print(Solution().romanToInt("LVIII"))
        