class Solution {
    private List<String> res = new ArrayList<>();
    private final static String[] digitToChar = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) {
            return res;
        }
        backtrack("", 0, digits);
        return res;
    }

    private void backtrack(String curStr, int i, String digits) {
        if (curStr.length() == digits.length()) {
            res.add(curStr);
            return;
        }

        String str = digitToChar[digits.charAt(i) - '0'];
        for (char ch : str.toCharArray()) {
            backtrack(curStr + ch, (i+1), digits);
        }
    }
}
