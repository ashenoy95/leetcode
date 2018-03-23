class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int j, k, sum;
        Arrays.sort(nums);
        int closest = nums[0] + nums[1] + nums[2];
        
        for(int i=0; i<nums.length-2; i++) {
            j = i+1;
            k = nums.length-1;
            while(j<k) {
                sum = nums[i]+nums[j]+nums[k];
                if(sum==target)
                    return target;
                if(sum<target) {
                    j++;
                } else {
                    k--;
                }
                if(Math.abs(target-sum)<Math.abs(target-closest))
                    closest = sum;
            }
        }
        
        return closest;
    }
}