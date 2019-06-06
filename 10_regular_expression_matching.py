class Solution:
    def isMatch(self, s, p):

        import re

        try:
            return re.compile(p).match(s).group(0) == s

        except AttributeError:
            return False
