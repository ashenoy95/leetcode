class Solution {
    public int longestSubstring(String s, int k) {
        HashMap<Character, Integer> char_count = new HashMap<>();
        int count, left, right, l = 0;
        
        for(int i=0; i<s.length(); i++) {
            if(!char_count.containsKey(s.charAt(i))) {
                char_count.put(s.charAt(i), 1);
            } else {
                count = char_count.get(s.charAt(i));
                char_count.put(s.charAt(i), count+1);
            }
        }
        
        while(l<s.length() && char_count.get(s.charAt(l))>=k) 
            l++;
        if(l==s.length())
            return l;
        
        left = longestSubstring(s.substring(0, l), k);
        right = longestSubstring(s.substring(l+1, s.length()), k);
        return Math.max(left, right);
    }
}