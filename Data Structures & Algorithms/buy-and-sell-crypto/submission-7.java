class Solution {
    public int maxProfit(int[] prices) {
        int l =0;
        int maxP = 0;

        for (int r = 1; r < prices.length; r++) {
            if (prices[r] > prices[l]) {
                int profit = prices[r] - prices[l];
                maxP = Math.max(profit, maxP);
            } else {
                l = r;
            }
        }
        return maxP;
    }
}
