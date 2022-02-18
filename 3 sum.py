class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_dict = {}
        used_dict = {}
        triplets_set = set()
        triplets_list = []
        for i in range(len(nums)):
            if nums[i] in my_dict.keys():
                my_dict[nums[i]].append(i)
            else:
                my_dict[nums[i]] = [i]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                key = -(nums[i] + nums[j])
                if key in my_dict.keys():
                    indexes = my_dict[key]
                    if len(indexes)>2:
                        cur_set = sorted([nums[i], nums[j], key]) 
                        a, b, c = cur_set[0], cur_set[1], cur_set[2]
                        if (a, b, c) not in triplets_set:
                            triplets_set.add((a, b, c))
                    elif len(indexes) == 2 and (indexes[0]!=i or indexes[1]!=j):
                        cur_set = sorted([nums[i], nums[j], key]) 
                        a, b, c = cur_set[0], cur_set[1], cur_set[2]
                        if (a, b, c) not in triplets_set:
                            triplets_set.add((a, b, c))
                    elif indexes[0]!=i and indexes[0]!=j:
                        cur_set = sorted([nums[i], nums[j], key]) 
                        a, b, c = cur_set[0], cur_set[1], cur_set[2]
                        if (a, b, c) not in triplets_set:
                            triplets_set.add((a, b, c))
        for triplet in triplets_set:
            triplets_list.append(list(triplet))
        return triplets_list