def decode_message( s: str, p: str) -> bool:
        m, n=len(s), len(p)
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True
        for j in range(1,n+1):
                if p[j-1]=='*':
                        dp[0][j]=dp[0][j-2]

# write your code here
  
        return False