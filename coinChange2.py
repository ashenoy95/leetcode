class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        OPT = [[0]*(amount+1) for i in range(len(coins)+1)]
        for i in range(1,amount+1):
            OPT[0][i] = 0
        for i in range(len(coins)+1):
            OPT[i][0] = 1
        for n in range(1,len(coins)+1):
            for w in range(1,amount+1):
                if coins[n-1]>w:
                    OPT[n][w] = OPT[n-1][w]
                else:
                    OPT[n][w] = OPT[n-1][w] + OPT[n][w-coins[n-1]]
        return OPT[len(coins)][amount]