public class SumNaturalNumbers {

    public static void main(String[] args) {
        int result = recursiveSummation(10);
        System.out.println(result);
    }
    
    public static int recursiveSummation(int inputNumber) {

        if (inputNumber <= 1) {
            return inputNumber;
        }
    
        return inputNumber + recursiveSummation(inputNumber - 1);
    }

}