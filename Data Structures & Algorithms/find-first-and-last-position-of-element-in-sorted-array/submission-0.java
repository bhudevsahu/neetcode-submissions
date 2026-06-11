class Solution {
    public int[] searchRange(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        int left = binarySearch(nums, l , r, target, true);
        int right = binarySearch(nums, l , r, target, false);
        return new int[]{left, right};
    }

    private int binarySearch(int[] nums, int l, int r, int target, boolean leftBiased) {
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