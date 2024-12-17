class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # create list to count frequency of each letter in sting s
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1 # count frequency of each letter by updating cnt
        
        # initialize empty list ans to store result and a variable j
        ans = []
        j = 24  # j will help to find next largest character

        # start from largets character and move back
        for i in range(25, -1, -1): # iterate through all letters from z to a
            j = min(i - 1, j) # update j to ensure it does not go lower than current
            while 1:

                # add character ascii lowercae to result until to reach reapeatlimit
                x = min(repeatLimit, cnt[i])
                cnt[i] -= x
                ans.append(ascii_lowercase[i] * x)
                # after using up all occurrences of current character, break it.
                if cnt[i] == 0:
                    break

                # need to find next character that still has occurences left 
                while j >= 0 and cnt[j] == 0:
                    j -= 1
                if j < 0:
                    break
                cnt[j] -= 1
                ans.append(ascii_lowercase[j])
        return "".join(ans)
