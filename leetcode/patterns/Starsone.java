public class Starsone {
    public static void main(String[] args) {

        int num = 10;
        for (int out = 1; out < num + 1; out++) {

            for (int inner = 0; inner < out; inner++) {
                System.out.print("*");
            }

            System.out.print("\n");
        }
    }
}
