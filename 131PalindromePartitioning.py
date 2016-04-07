class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        if not s:
            return self.res
        if len(s) == 1:
            self.res.append([s])
            return self.res
            
        back = 0
        front = 0
        end = len(s)
        dict_pali = {}
        
        #find all palindrome 
        for idx in range(end):
            back = idx-1
            front = idx+1
            while back >=0 and front < end and s[back] == s[front]:
                if back in dict_pali:
                    dict_pali[back].append(s[back:front+1])
                else:
                    dict_pali[back] = [s[back:front+1]]
                back -= 1
                front += 1
                
            front = idx + 1
            back = idx
            while back >=0 and front < end and s[back] == s[front]:
                if back in dict_pali:
                    dict_pali[back].append(s[back:front+1])
                else:
                    dict_pali[back] = [s[back:front+1]]
                back -= 1
                front += 1
     
        temp = []

        idx = 0
        self.pali_part(s,dict_pali,idx,temp,end)

        return self.res
       
    def pali_part(self,s,dict,idx,temp,end):
        if idx >= end:
            self.res.append(temp)
            return 
        if idx in dict: 
            for pali in dict[idx]:
                self.pali_part(s, dict, idx+len(pali), temp+[pali],end)
        self.pali_part(s, dict, idx+1, temp+[s[idx]],end)
        
            
    



sol = Solution()
s = "cbbbcc"
print sol.partition(s)            
        
        
        
                
    