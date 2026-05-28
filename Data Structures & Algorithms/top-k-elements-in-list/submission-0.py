class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}

        # get the frequency of each number via hashmap
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        # lambda x : x[1] returns the frequency count ... ex: { 1 : 2 } => x[1] = 2
        output_list = sorted(frequency_dict.items(), key=lambda x:x[1], reverse=True)

        # counts_list = sorted(counts.items(), key=lambda x:x[1], reverse=True)
        sorted_freq = dict(output_list[:k])
        return [num for num in sorted_freq]



        