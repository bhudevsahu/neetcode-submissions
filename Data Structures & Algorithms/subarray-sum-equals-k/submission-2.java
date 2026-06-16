class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> preMap = new HashMap<>();
        preMap.put(0, 1);
        int curSum = 0, res = 0;

        for(int num: nums) {
            curSum += num;
            int diff = curSum - k;

            res += preMap.getOrDefault(diff, 0);
            preMap.put(curSum, preMap.getOrDefault(curSum, 0) + 1);
        }

        return res;
    }
}