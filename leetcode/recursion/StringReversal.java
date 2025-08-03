
public class StringReversal {
    

    public static void main(String[] args) {

            System.out.println(recurse("tubby"));
    }


    static String recurse(String input){
        if(input.length() == 0) {
            return "";
        }

        return recurse(input.substring(1)) + input.charAt(0); 
    }

}