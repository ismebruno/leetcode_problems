class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        converted = 0
        last_added = 0
        for i in range(len(s))[::-1]:
            if numerals[s[i]] >= last_added:
                converted += numerals[s[i]]
                last_added = numerals[s[i]]
            elif numerals[s[i]] <= last_added:
                converted -= numerals[s[i]]
        return converted
