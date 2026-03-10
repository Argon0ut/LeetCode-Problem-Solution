class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequency of each element
        # put them into minHeap
        # cut all the elements after exceeding k --> pops out the smallest elements everytime

        elems = {}
        minHeap = []

        for num in nums:
            elems[num] = elems.get(num, 0) + 1

        for key, value in elems.items():
            heapq.heappush(minHeap, (value, key))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        counter = 0
        for val, key in minHeap:
            if counter == k:
                return res
            res.append(key)
            counter += 1

        return res