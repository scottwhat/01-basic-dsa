package sort;

public class RecursiveMergeSort {

    public static void main(String[] args) {

        int[] data = new int[]{-5,20,10,2,3,0};
        mergeSort(data, 0, data.length -1);
        System.out.println("stop");
        
    }

    static void mergeSort(int[] data, int start, int end){ 
        if(start < end){
            int mid = (start + end) / 2;
            //left
            mergeSort(data, start, mid);
            
            //right
            mergeSort(data, mid + 1, end);

            merge(data, start, mid, end);
        }
        
    }


    public static void merge(int[] data, int start, int mid, int end) {

        //build a temporary array to avoid modifying the original contents

        int[] temp = new int[end-start + 1];


        //k = tracker variable 
        int i = start, j = mid + 1, k = 0;

        //while both sub arrays have values try to merge in sorted order 
        while(i <= mid && j <= end) {
            if( data[i] <= data[j]) {
                temp[k] = data[i];
                i++;
                k++;
            }

            else {
                temp[k] = data[j];
                k++;
                j++;
            }

            //add rest of values from left subarry if right empty
            while (i <= mid) {
                temp[k] = data[i];
                k++;
                i++;
                
            }

            while( j <= end) {
                temp[k] = data[j];
                k++;
                j++;
            }

            
            //copying temp vals into the data array finally 
            for(i = start; i <= end; i++) {
                data[i] = temp[i - start];
            }

        }

    }



    

    
}
