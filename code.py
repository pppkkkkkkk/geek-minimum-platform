class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        n = len(arr)
        if n == 0: return 0
        
        merged = []
        for i in range(n):
            merged.append([arr[i],'A'])
            merged.append([dep[i],'D'])
            
        merged.sort()
        
        result = 0
        platform = 0
        for i in range(len(merged)):
            if merged[i][1] == 'A':
                platform+=1
                result = max(platform, result)
            else:
                platform-=1
        return result
            
            
        
        