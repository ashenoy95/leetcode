class Solution {
    public String longestPalindrome(String s) {
        boolean flag = true;
        int start = 0, end = 0, longest = 0;
        boolean[][] OPT = new boolean[s.length()][s.length()];
        
        for(int i=0; i<s.length()-1; i++) {
            if(s.charAt(i)!=s.charAt(i+1)) {
                flag = false;
                break;
            }
        }
        if(flag)
            return s;
        
        for(int i=0; i<s.length(); i++) {
            for(int j=0; j<s.length(); j++) {
                if(i==j) {
                    OPT[i][j] = true;
                } else if(j==i+1) {
                    if(s.charAt(i)==s.charAt(j)) {
                        OPT[i][j] = true;
                    } else {
                        OPT[i][j] = false;
                    }
                } else {
                    OPT[i][j] = false;
                }
                
                if(OPT[i][j]) {
                     if(j-i+1>longest) {
                        longest = j-i+1;
                        start = i;
                        end = j+1;
                    }
                }
            }
        }
        
        for(int j=2; j<s.length(); j++) {
            for(int i=0; i<j-1; i++) {
                if((s.charAt(i)==s.charAt(j)) && (OPT[i+1][j-1]==true)) {
                    OPT[i][j] = true;
                    if(j-i+1>longest) {
                        longest = j-i+1;
                        start = i;
                        end = j+1;
                    }
                }
            }
        }
        
        return s.substring(start, end);
    }
}