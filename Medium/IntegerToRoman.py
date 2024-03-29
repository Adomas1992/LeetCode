class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not 1 <= num <= 3999:
            raise ValueError("Input must be between 1 and 3999 inclusive")

        roman_numeral = ""
        roman = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I",
        }

        for value, symbol in sorted(roman.items(), key=lambda x: x[0], reverse=True):
            while num >= value:
                roman_numeral += symbol
                num -= value

        return roman_numeral
        

solution = Solution()
result = solution.intToRoman(1994)
print(result)