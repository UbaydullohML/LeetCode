class Solution:
    def romanToInt(self, s: str) -> int:
        # hash map
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        n = len(s)

        # iteration through string
        for i in range(n):
          current_value = roman_map[s[i]]
          # operation
          if i + 1 < n and current_value < roman_map[s[i+1]]:
            total -= current_value
          else:
            total += current_value
        return total
