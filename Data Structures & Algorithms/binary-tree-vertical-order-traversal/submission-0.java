/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private static class Entry {
        TreeNode node;
        int col;

        Entry(TreeNode node, int col) {
            this.node = node;
            this.col = col;
        }
    }

    public List<List<Integer>> verticalOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();

        Map<Integer, List<Integer>> cols = new TreeMap<>();
        Queue<Entry> q = new LinkedList<>();

        q.offer(new Entry(root, 0));

        while(!q.isEmpty()) {
            Entry e = q.poll();

            cols.computeIfAbsent(e.col, k -> new ArrayList<>()).add(e.node.val);

            if (e.node.left != null) {
                q.offer(new Entry(e.node.left, e.col - 1));
            }
            if (e.node.right != null) {
                q.offer(new Entry(e.node.right, e.col + 1));
            }
        }

        return new ArrayList<>(cols.values());
    }
} 