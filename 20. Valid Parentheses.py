class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        stk = []
        
        for ch in s:
            if ch in hmap:
                stk.append(hmap[ch])
            elif stk and ch == stk[-1]:
                stk.pop()
            else:
                return False
                
        return stk == []