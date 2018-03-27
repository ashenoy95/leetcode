class Solution {
    public String convert(String s, int numRows) {
        String zigzag = "";
        String[] zigzag_list = new String[numRows];
        ArrayList<String> l = new ArrayList<>(3);
        boolean flag = true;
        int row = 0;
        
        if(s=="")
            return "";
        if(s.length()<numRows || numRows==1) 
            return s;
        
        Arrays.fill(zigzag_list, "");
        
        for(int i=0; i<s.length(); i++) {
            zigzag_list[row] += s.charAt(i);
            if(flag) {
                row++;
            } else {
                row--;
            }
            if(row==numRows) {
                flag = false;
                row = numRows-2;
            } 
            if(row==-1) {
                flag = true;
                row = 1;
            }
        }

        for(int i=0;i<numRows; i++) 
            zigzag += zigzag_list[i];
        
        return zigzag;
        
    }
}