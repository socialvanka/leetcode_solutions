class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        no_swap = 0
        swap = 1
        for i in range(1, n):
            new_no_swap = new_swap = float('inf')
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                new_no_swap = min(new_no_swap, no_swap)
                new_swap = min(new_swap, swap + 1)
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                new_no_swap = min(new_no_swap, swap)
                new_swap = min(new_swap, no_swap + 1)
            no_swap = new_no_swap
            swap = new_swap
        return min(no_swap, swap)
