class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> str_rep = new ArrayList<>();
        for(int i=1; i<=n; i++) {
            if(i%3==0 && i%5==0) {
                str_rep.add("FizzBuzz");
            } else if(i%3==0 && i%5!=0) {
                str_rep.add("Fizz");
            } else if(i%5==0 && i%3!=0) {
                str_rep.add("Buzz");
            } else {
                str_rep.add(Integer.toString(i));
            }
        }
        return str_rep;
    }
}