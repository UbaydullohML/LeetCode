from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        for i in arr:
            if counts[i] == 1:
                k-=1
                if k == 0:
                    return i
        return ""
