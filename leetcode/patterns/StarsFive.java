package patterns;

//expected output: 
public class StarsFive {

    public static void main(String[] args) {
        pattern5(5);
    }

    static void pattern5(int n) {
        // runs 2n-1 times
        for (int row = 0; row < 2 * n; row++) {

            int totalColsInRow = row > n ? 2 * n - row : row;

            // how many columns
            for (int col = 0; col < totalColsInRow; col++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

}
