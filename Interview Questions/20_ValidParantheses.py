class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k = []
        for i in s:
            if(i=='(' or i =='{' or i =='['):
                k.append(i)
            elif(i==')' or i =='}' or i ==']'):
                if(len(k) == 0):
                    return False
                element = k.pop()
                if(i==')' and element!='('):
                    return False
                elif(i==']' and element!='['):
                    return False
                elif(i=='}' and element!='{'):
                    return False
        if(len(k)!=0):
            return False
        return True
        
