class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        s = set(candies)
        l = len(candies)
        return min(len(s),int(l/2))

        #len(s)>=l/2  则return l/2
        #<l/2  return len(s)