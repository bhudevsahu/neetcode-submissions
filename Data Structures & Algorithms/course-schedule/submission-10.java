class Solution {
    Map<Integer, List<Integer>> preMap = new HashMap<>();
    Set<Integer> visiting = new HashSet<>();


    // [[0,1], [1, 3], [2, 3]]

    public boolean canFinish(int numCourses, int[][] prerequisites){
        for (int i = 0; i < numCourses; i++) {
            preMap.put(i, new ArrayList<>());
        }

        for(int[] pre : prerequisites) {
            preMap.get(pre[0]).add(pre[1]);
        }

        for (int c=0; c < numCourses; c++) {
            if (!dfs(c)) {
                return false;
            }
        }
        return true;
    }

    private boolean dfs(int crs) {
        if (visiting.contains(crs)) {
            return false;
        }

        if (preMap.get(crs).isEmpty()) {
            return true;
        }

        visiting.add(crs);
        for(int c : preMap.get(crs)) {
            if (!dfs(c)) {
                return false;
            }
        }
        visiting.remove(crs);
        preMap.put(crs, new ArrayList<>());
        return true;
    }
}
