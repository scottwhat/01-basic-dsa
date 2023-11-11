public class ZeroCount {
    
    public static void main(String[] args) {
        System.out.println(ZeroCount(2010));
    }

    static int ZeroCount(int n) {
        return helper(n, 0);
    }

    private static int helper(int n, int c){
        //base case once all zeros counted 
        if (n == 0){
            return c;
        }

        int rem = n % 10;
        if( rem == 0) {
            return helper(n / 10, c + 1);
        }

        return helper(n/10, c);
    }
}
