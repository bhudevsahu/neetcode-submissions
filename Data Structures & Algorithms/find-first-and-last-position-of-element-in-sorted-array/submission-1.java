class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left = binarySearch(nums, target, true);
        int right = binarySearch(nums, target, false);
        return new int[]{left, right};
    }

    private int binarySearch(int[] nums, int target, boolean leftBiased) {
        int l = 0, r = nums.length - 1;
        int i = -1;
        while (l <= r) {
            int m = (l + r) / 2;

            if (target > nums[m]){
                l = m+1;
            } else if (target < nums[m]) {
                r = m - 1;
            } else {
                i = m;
                if (leftBiased) r = m - 1;
                else l = m + 1;
            }
        }
        return i;
    }
}