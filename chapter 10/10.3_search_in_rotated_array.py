


def rotatedSearch(nums, target):



    def bst(start, end, nums, target):
        if start > end:
            return None
        mid = (start + end ) // 2

        if nums[mid] == target:
            return mid

        if nums[start] < nums[mid]:
            if nums[start] <= target and target < nums[mid]:
                return bst(start, mid, nums, target)
            else:
                return bst(mid + 1, end, nums, target)
        elif nums[mid] < nums[end]:
            if target > nums[mid] and target <= nums[end]:
                return bst(mid + 1, end, nums, target)
            else:
                return bst(mid + 1, end, nums, target)
        else:
            location = None
            if nums[start] == nums[mid]:
                location = bst(start, mid, nums, target)
            if location == None and nums[mid] == nums[end]:
                location = bst(mid + 1, end, nums, target)
            return location



    return bst(0, len(nums) - 1, nums, target)


print(rotatedSearch([1, 2, 3, 4, 5], 4))