class Solution {
    private Map<Integer, List<Integer>> preMap = new HashMap<>();
    private Set<Integer> visited = new HashSet<>();
    private Set<Integer> processed = new HashSet<>();
    private List<Integer> output = new ArrayList<>();

    public int[] findOrder(int numCourses, int[][] prerequisites) {        
        for (int i = 0; i < numCourses; i++) {
            preMap.put(i, new ArrayList<>());
        }
        
        for (int[] pre : prerequisites) {
            preMap.get(pre[0]).add(pre[1]);
        }

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i)) {
                return new int[0];
            }
        }

        int[] res = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            res[i] = output.get(i);
        }

        return res;
    }

    private boolean dfs(int crs) {
        if (visited.contains(crs)) {
            return false;
        }

        if (processed.contains(crs)) {
            return true;
        }

        visited.add(crs);
        for (int c : preMap.get(crs)) {
            if (!dfs(c)) {
                return false;
            }
        }
        output.add(crs);
        processed.add(crs);
        visited.remove(crs);
        return true;
    }
}
