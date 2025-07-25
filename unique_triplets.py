def triplet_sum(nums, key):
    NEW_LIST = []
    seen = set()  # to store unique sorted triplets

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sums = nums[i] + nums[j] + nums[k]
                if sums == key:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if triplet not in seen:
                        seen.add(triplet)
                        NEW_LIST.append(list(triplet))
    return NEW_LIST

nums = [1, 1, 2, 3, 4, 4, 5, -5, -1]
key = 7
print(triplet_sum(nums, key))
