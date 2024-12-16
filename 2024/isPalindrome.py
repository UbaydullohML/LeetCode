# 9. Palindrome Number
class Solution(object):
  def isPalindrome(self,x):
        """
        :type x: int
        :rtype: bool
        """
    # if number is negative, make it false
    if x < 0:
      return False
    
    #convert number to string
    strx = str(x)

    # initialize pointers
    left = 0 
    right = len(strx) - 1

    # two pointers comparison
    while left < right:
      if strx[left] != strx[right]:
        return False
      left += 1
      right -= 1
    return True
