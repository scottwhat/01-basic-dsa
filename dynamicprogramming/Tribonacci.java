package dynamicprogramming;

import java.util.HashMap;

public class Tribonacci {

    public static void main(String[] args) {
        System.out.println(Fib.fib(7));    
    }

    public static int fib(int n) {
        return fib(n,new HashMap<>());

    }
    public static int fib(int n, HashMap<Integer, Integer> memo){
        if (n == 0 || n == 1) {
            return n;
        }


        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        int result = fib(n - 1, memo) + fib(n - 2, memo) + fib(n - 3, memo);
        memo.put(n, result);
        return result;
    }
    
}
