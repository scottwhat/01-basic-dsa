public class PrintStars {

    public static void main(String[] args) {
        printStars(5);
    }

    static void printStars(int starsNum) {
        if(starsNum == 0){
            return;
        }
        printStars(--starsNum);

        for(int i = 0; i <= starsNum; i++) {
            System.out.print('*');
        }
        System.out.println("");



    }
    
}
