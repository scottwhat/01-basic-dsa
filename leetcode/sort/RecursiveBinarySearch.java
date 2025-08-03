package sort;

public class RecursiveBinarySearch {

    public static void main(String[] args) {
        
    }

    public static int binarySearch(int[] A, int left, int right, int x) {
        //check if valid search space
        if(left > right) {
            return -1;
        }


        int mid = (left + right) / 2;

        //found
        if (x == A[mid]){
            return mid;
        }
        // reduce and keep left half of array
        if( x < A[mid]){
            return binarySearch(A, left, mid - 1, x);
        
        }

        //value on right half, Mid + 1s
        return binarySearch(A, mid + 1, right, x);
    }
    
}
