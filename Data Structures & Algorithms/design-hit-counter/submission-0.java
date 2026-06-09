class HitCounter {
    private Queue<Integer> hits;

    public HitCounter() {
        this.hits = new LinkedList<>();
    }
    
    public void hit(int timestamp) {
        this.hits.add(timestamp);
    }
    
    public int getHits(int timestamp) {
        while(!this.hits.isEmpty() && timestamp - this.hits.peek() >= 300) {
            this.hits.poll();
        }
        return this.hits.size();
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */
