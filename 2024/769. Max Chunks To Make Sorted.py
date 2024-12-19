# 769. Max Chunks To Make Sorted

class Solution(object):
    def maxChunksToSorted(self, arr):
        max_so_far = 0  # Keep track of the largest number seen so far
        chunks = 0      # Count the chunks

        for i in range(len(arr)):
            max_so_far = max(max_so_far, arr[i])  # Update the largest number seen
            # 	•	If arr[i] is larger, max_so_far becomes arr[i].
            if max_so_far == i:  # If the largest number matches the current index
                chunks += 1      # We can form a chunk here

        return chunks
            
