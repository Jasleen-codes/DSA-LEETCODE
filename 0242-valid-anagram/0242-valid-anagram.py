class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
                count = {}
                if len(s)!=len(t):
                    return False
                for ch in s:
                    count[ch] = count.get(ch,0)+1
                # removing characters using t
                for ch in t:
                    if ch not in count:
                        return False
                    count[ch]-=1
                    if count[ch]==0:
                        del count[ch]
                return len(count)==0
