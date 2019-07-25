class Solution {

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] nums3 = new int[nums1.length+nums2.length];
        int counter1 = 0, counter2 = 0;
        double s;

        for(int i = 0; i < nums1.length; i++){
            while(true){
                if((counter1 < nums2.length)&&(nums2[counter1] < nums1[i])){
                    nums3[counter2] = nums2[counter1];
                    counter1++;
                    counter2++;
                }
                else{
                    nums3[counter2] = nums1[i];
                    counter2++;
                    break;
                }
                
            }
        }
        
        if(counter1<nums2.length){
            for(int i = counter2; i < nums3.length; i++){
                nums3[i] = nums2[counter1];
                counter1++;
            }
        }
        

        if(nums3.length % 2 == 0){
            s = (nums3[nums3.length/2-1]+nums3[nums3.length/2]);
            s = s/2;
        }
        else{
            s = nums3[nums3.length/2];
  
        }
        
        return s;
    }
}
