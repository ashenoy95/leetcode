class Solution {
    public void generate(String combo, List<String> combos, int left, int right, int n) {
        if(left==n && right==n) {
            combos.add(combo);
        } else {
            if(left<n)
                generate(combo+"(", combos, left+1, right, n);
            if(right<left)
                generate(combo+")", combos, left, right+1, n);
        }
    }
    
    public List<String> generateParenthesis(int n) {
        ArrayList<String> combos = new ArrayList<>();
        generate("", combos, 0, 0, n);
        return combos;
    }
}