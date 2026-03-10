class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        res = []

        counter = 0
        for elem in strs:
            x = ''.join(sorted(elem))

            if x not in anagrams:
                anagrams[x] = counter
                res.append([elem])
                counter += 1
            else:
                res[anagrams[x]].append(elem)

        return res