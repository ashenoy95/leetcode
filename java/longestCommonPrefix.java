class Solution {
    public String findPrefix(String str1, String str2) {
        int i = 0, j = 0;
        String prefix = "";
        
        while(i<str1.length() && j<str2.length()) {
            if(str1.charAt(i)!=str2.charAt(j))
                break;
            prefix += str1.charAt(i);
            i++;
            j++;
        }
        
        return prefix;
    }
    
    public String longestCommonPrefix(String[] strs) {
        if(strs.length==0)
            return "";
        
        String prefix = strs[0];
        
        for(int i=0; i<strs.length; i++)
            prefix = findPrefix(prefix, strs[i]);
        
        return prefix;
    }
}