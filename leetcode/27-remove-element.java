class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;

        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[k]);
            if (nums[i] != val) {
                nums[k] = nums[i];
                System.out.println(nums);
                k++;
            }
        }

        return k;
    }
}
