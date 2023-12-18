package dynamicprogramming;

public class MinChange {

    public static int MinChange(int amount, List<Integer> coins) {

        if (amount == 0) {
            return 0;
        }

        int minCoins = -1;
        // declar as false
        for (int coin : coins) {
            int subAmount = amount - coin;
            int subCoins = MinChange(subAmount, coins);

            if (subCoins != -1) {
                int numCoins = subCoins + 1;
                if (numCoins < minCoins) {
                    minCoins = numCoins;
                }
            }
        }

    }

}
