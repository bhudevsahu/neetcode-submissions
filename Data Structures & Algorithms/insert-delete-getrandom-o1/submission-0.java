class RandomizedSet {
    Map<Integer, Integer> numMaps;
    List<Integer> numList;
    Random rand;

    public RandomizedSet() {
        this.numMaps = new HashMap<>();
        this.numList = new ArrayList<>();
        rand = new Random();
    }
    
    public boolean insert(int val) {
        if (numMaps.containsKey(val)) return false;
        numMaps.put(val, numList.size());
        numList.add(val);
        return true;        
    }
    
    public boolean remove(int val) {
        if (!numMaps.containsKey(val)) return false;
        int idx = numMaps.get(val);
        int lastVal = numList.get(numList.size() - 1);
        numList.set(idx, lastVal);
        numMaps.put(lastVal, idx);
        numList.remove(numList.size() - 1);
        numMaps.remove(val);
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