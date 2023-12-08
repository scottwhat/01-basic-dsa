package patterns;

public class Nums30 {

    public static void main(String[] args) {
        pattern(5);
    }

    static void pattern(int n) {

        // use to subtract the distance calc from the N input
        int originalN = n;

        n = 2 * n;

        for (int row = 0; row <= n; row++) {
            for (int col = 0; col <= n; col++) {
                int atEveryIndex = originalN - Math.min(Math.min(row, col), Math.min(n - row, n - col));
                System.out.print(atEveryIndex + " ");

            }
            System.out.println();
        }
    }

}
