class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        mapS = self.countLetters(s)
        mapT = self.countLetters(t)

        return mapS == mapT

        

    def countLetters(self, word: str):
        hash_map = {}

        for s in word:
            if s in hash_map:
                hash_map[s] += 1
            else:
                hash_map[s] = 1
        return hash_map     