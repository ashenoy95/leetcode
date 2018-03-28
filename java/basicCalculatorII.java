class Solution {
    public String operate(int v1, int v2, char op) {
        int res;
        
        if(op=='/') {
            res = v1/v2;
        } else if(op=='*') {
            res = v1*v2;
        } else if(op=='+') {
            res = v1 + v2;
        } else {
            res = v1 - v2;
        }
        
        return Integer.toString(res);
    }
    
    
    public int calculate(String s) {
        Stack<String> stack1 = new Stack<>();
        Stack<Character> stack2 = new Stack<>();
        String temp = "";
        char op;
        int v1=0, v2=0, res=0;
        
        HashMap<Character, Integer> operators = new HashMap<>();
        operators.put('+', 0);
        operators.put('-', 0);
        operators.put('*', 1);
        operators.put('/', 1);
        
        for(char c: s.toCharArray()) {
            if(c==' ')
                continue;
            
            if(!operators.containsKey(c)) {
                temp += c;
            } else {
                stack1.push(temp);
                temp = "";
                while(!stack2.empty() && operators.get(stack2.peek())>=operators.get(c)) {
                    op = stack2.pop();
                    v2 = Integer.parseInt(stack1.pop());
                    v1 = Integer.parseInt(stack1.pop());
                    stack1.push(operate(v1, v2, op));
                }
                stack2.push(c);
            }   
        }
        
        if(temp!=" ") 
            stack1.push(temp);
        
        while(!stack2.empty()) {
            op = stack2.pop();
            v2 = Integer.parseInt(stack1.pop());
            v1 = Integer.parseInt(stack1.pop());
            stack1.push(operate(v1, v2, op));
        }
        
        return Integer.parseInt(stack1.peek());
    }
}