public class Fib {
    
    public static void main(String[] args) {
        long fibResult = fib(8);
        System.out.println(fibResult);
    }

    static long fib(long n) {
        if((n == 0) || (n == 1)){
            return n;
        }

        else{
            return fib(n-1) + fib(n-2);
        }
    }
}
