class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        int temp;
        for(int i=0; i < nums.length; i++){
            for(int j=i+1;j<nums.length;j++){
                temp = nums[i]+nums[j];
                if(temp==target){
                    ans[0] = i;
                    ans[1] = j;
                    break;
                }
            }
        }
        return ans;
    }
}
