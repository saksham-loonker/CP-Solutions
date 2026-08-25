class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = list(word1)
        w2 = list(word2)
        final = []
        while w1 or w2:
            if w1:
                final.append(w1.pop(0))
            if w2:
                final.append(w2.pop(0))
        joint = "".join(final)
        return joint

