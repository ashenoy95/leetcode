class Solution {
    public int coinChange(int[] coins, int amount) {
        int[][] OPT = new int[coins.length+1][amount+1];
        for(int[] row: OPT) 
            Arrays.fill(row, -1);
        for(int i=0; i<=coins.length; i++)
            OPT[i][0] = 0;
        
        for(int i=1; i<=coins.length; i++) {
            for(int j=1; j<=amount; j++) {
                if(j<coins[i-1]) {
                    OPT[i][j] = OPT[i-1][j];
                } else if(j==coins[i-1]) {
                    OPT[i][j] = 1;
                } else if(OPT[i-1][j]==-1 && OPT[i][j-coins[i-1]]==-1) {
                    OPT[i][j] = -1;
                } else if(OPT[i-1][j]==-1) {
                    OPT[i][j] = OPT[i][j-coins[i-1]] + 1;
                } else if(OPT[i][j-coins[i-1]]==-1) {
                    OPT[i][j] = OPT[i-1][j];
                } else {
                    OPT[i][j] = Math.min(OPT[i-1][j], OPT[i][j-coins[i-1]] + 1);
                }
            }
        }
        return OPT[coins.length][amount];
    }
}