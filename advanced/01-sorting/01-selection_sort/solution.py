class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            if i != min_index:
                nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [7, 4, 1, 5, 3],        # normal case
        [5, 4, 4, 1, 1],        # duplicates
        [1, 2, 3, 4, 5],        # already sorted
        [5, 4, 3, 2, 1],        # reverse sorted
        [],                     # empty array
        [1]                     # single element
    ]

    for nums in test_cases:
        original = nums.copy()
        sorted_nums = solution.selectionSort(nums)
        print(f"Input: {original} -> Sorted: {sorted_nums}")
