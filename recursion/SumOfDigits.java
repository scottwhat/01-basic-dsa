public class SumOfDigits {
    

    public static void main(String[] args) {
        
    }

    static int sumDigits(int n){
        if(n == 0){
            return 0;
        }
        
        return( n % 10) + sumDigits(n / 10);
    }
}
