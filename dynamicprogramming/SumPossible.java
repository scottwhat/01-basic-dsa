package dynamicprogramming;

import java.util.List;
import java.util.HashMap;

//brute force
public class SumPossible {
    public static boolean sumPossible(int amount, List<Integer> numbers) {
        return sumPossible(amount, numbers, new HashMap<>());
    }

    // helper
    public static boolean sumPossible(int amount, List<Integer> numbers, HashMap<Integer, Boolean> memo) {

        if (amount == 0) {
            return true;

        }

        if (amount < 0) {
            return false;
        }

        if (memo.containsKey(amount)) {

            return memo.get(amount);
        }

        // recursive call for every num of the list but its going into memo
        for (int num : numbers) {
            int subAmount = amount - num;

            if (sumPossible(subAmount, numbers, memo)) {
                memo.put(amount, true);
                return true;
            }
        }

        // late return false only if all recursive cases have run
        memo.put(amount, false);
        return false;

    }

    public static void main() {
        // this function behaves as `main()` for the 'run' command
        // you may sandbox in this function , but should not remove it
    }

}
