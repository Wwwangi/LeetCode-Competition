class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] counter = new int[s.length()];
        int index, max=0, det = 0;
        
        if(s.length()==0) return 0;

        for(int i = 0; i < s.length(); i++){
            det = 0;
            for(int j = i+1; j < s.length(); j++){
                for(int k = i; k<j; k++){
                    if(s.charAt(k)==s.charAt(j)){
                        det = 1;
                        break;
                    }
                }
                if(det == 0){
                    counter[i]++;
                }
                else break;
            }
            
            if(i == 0) max = counter[0];
            else if((i!=0)&&(counter[i]>max)){
                max = counter[i];
                index = i;
            }
        }

        return max+1;
    }
}
