/**
Test cases:
1. Success case - hit is being added and we can retrieve the get hits.
2. Edge cases - get hits without adding any hits
3. The counter should evict all the timestamps that are more than 300 at the time of getHits call.

*/

class HitCounter {
    Queue<Integer> hits;

    public HitCounter() {
        hits = new LinkedList<>();        
    }
    
    public void hit(int timestamp) {
        this.hits.add(timestamp);
    }
    
    public int getHits(int timestamp) {
        while(!this.hits.isEmpty() && timestamp - this.hits.peek() >= 300) {         
            this.hits.remove();
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
