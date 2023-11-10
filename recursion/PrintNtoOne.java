public class PrintNtoOne {

    public static void main(String[] args) {
    printNToOne(5);
    }
    

    static void printNToOne(int n){

        if(n == 0){
            return;
        }

        printNToOne(n - 1);
        System.out.println(n);

    }
}
