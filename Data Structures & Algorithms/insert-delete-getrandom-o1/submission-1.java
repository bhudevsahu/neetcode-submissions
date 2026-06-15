class RandomizedSet {
    private Map<Integer, Integer> numMap;
    private List<Integer> numList;
    private Random rand;

    public RandomizedSet() {
        numMap = new HashMap<>();
        numList = new ArrayList<>();
        rand = new Random();
    }
    
    public boolean insert(int val) {
        if (numMap.containsKey(val)) return false;
        numMap.put(val, numList.size());
        numList.add(val);
        return true;        
    }
    
    public boolean remove(int val) {
        if (!numMap.containsKey(val)) return false;
        int idx = numMap.get(val);
        int last = numList.get(numList.size() - 1);
        numList.set(idx, last);
        numMap.put(last, idx);
        numList.remove(numList.size() - 1);
        numMap.remove(val);
        return true;
    }
    
    public int getRandom() {
        return numList.get(rand.nextInt(numList.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */