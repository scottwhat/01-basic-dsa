
public class Palindrome {
    

    public static void main(String[] args) {

            System.out.println(pal("kayak"));
    }


    static Boolean pal(String input){
        if (input.length() == 0 || input.length() == 1) {
            return true;
        }

        String s = "aB".toLowerCase();
        if(input.charAt(0) == input.charAt(input.length() - 1)){
            return pal(input.substring(1, input.length() -1));
        }

        return false;

}
}

