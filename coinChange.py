class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        OPT = [[-1]*(amount+1) for i in range(len(coins)+1)]
        for i in range(len(coins)+1):
	        OPT[i][0] = 0
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j<coins[i-1]:
                    OPT[i][j] = OPT[i-1][j]
                elif j==coins[i-1]:
                    OPT[i][j] = 1
                elif OPT[i-1][j]==-1 and OPT[i][j-coins[i-1]]==-1:
                    OPT[i][j] = -1
                elif OPT[i-1][j]==-1:
                    OPT[i][j] = OPT[i][j-coins[i-1]]+1
                elif OPT[i][j-coins[i-1]]==-1:
                    OPT[i][j] = OPT[i-1][j]
                else:
                    OPT[i][j] = min(OPT[i-1][j], OPT[i][j-coins[i-1]]+1)
        return OPT[len(coins)][amount]
                    