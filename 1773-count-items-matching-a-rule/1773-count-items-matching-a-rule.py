class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # print (ruleKey, ruleValue)
        if ruleKey == "type":
            i = 0
        elif ruleKey == "color":
            i = 1
        else:
            i = 2
        counter = 0
        for j in items:
            # print (j[i])
            if j[i] == ruleValue:
                counter += 1
        return counter