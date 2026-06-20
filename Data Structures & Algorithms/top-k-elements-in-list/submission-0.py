class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        res = []

        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1
        
        sorted_map = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse = True))

        for key, values in sorted_map.items():
            if k != 0:
                res.append(key)
                k -= 1
        return res

        