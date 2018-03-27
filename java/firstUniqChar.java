class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> char_counts = new HashMap<>();
        int count;
        
        for(int i=0; i<s.length(); i++) {
            if(!char_counts.containsKey(s.charAt(i))) {
                char_counts.put(s.charAt(i), 1);
            } else {
                count = char_counts.get(s.charAt(i));
                char_counts.put(s.charAt(i), count+1);
            }
        }
        
        for(int i=0; i<s.length(); i++) {
            if(char_counts.get(s.charAt(i))==1)
                return i;
        }
        return -1;
    }
}