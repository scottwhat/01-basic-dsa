public class DecToBinary {

    public static void main(String[] args) {

        String done = findBinary(233,"");
        System.out.println(done);
        
    }


    public static String findBinary(int decimal, String result){

        if(decimal == 0) {
            return result;
        }

        result = decimal % 2 + result;
        return findBinary(decimal / 2, result);
    }
}
