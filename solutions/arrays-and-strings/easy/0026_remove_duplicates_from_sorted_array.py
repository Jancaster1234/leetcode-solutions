"""
26. Remove Duplicates from Sorted Array
Difficulty: Easy
Date Solved: 2026-02-09
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

Problem Description:
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of
the elements should be kept the same. Then return the number of unique elements in nums.

Approach:
- Use two pointers technique
- Since array is sorted, duplicates are adjacent
- Left pointer (k) tracks position for next unique element
- Right pointer iterates through array
- Only update position k when we find a new unique element (nums[i] != nums[k-1])
- Return k as the count of unique elements

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Remove duplicates in-place and return new length.
        """
        if not nums:
            return 0

        k = 1  # First element is always unique, start from index 1

        # Iterate from second element
        for i in range(1, len(nums)):
            # If current element is different from previous unique element
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    assert k1 == 2, f"Expected k=2, got k={k1}"
    assert nums1[:k1] == [1, 2], f"Expected [1,2], got {nums1[:k1]}"
    print(f"✓ Test 1 passed: k={k1}, nums={nums1[:k1]}")

    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    assert k2 == 5, f"Expected k=5, got k={k2}"
    assert nums2[:k2] == [0, 1, 2, 3, 4], f"Expected [0,1,2,3,4], got {nums2[:k2]}"
    print(f"✓ Test 2 passed: k={k2}, nums={nums2[:k2]}")

    # Test case 3: Single element
    nums3 = [1]
    k3 = sol.removeDuplicates(nums3)
    assert k3 == 1, f"Expected k=1, got k={k3}"
    assert nums3[:k3] == [1], f"Expected [1], got {nums3[:k3]}"
    print(f"✓ Test 3 passed: k={k3}, nums={nums3[:k3]}")

    # Test case 4: All duplicates
    nums4 = [1, 1, 1, 1, 1]
    k4 = sol.removeDuplicates(nums4)
    assert k4 == 1, f"Expected k=1, got k={k4}"
    assert nums4[:k4] == [1], f"Expected [1], got {nums4[:k4]}"
    print(f"✓ Test 4 passed: k={k4}, nums={nums4[:k4]}")

    # Test case 5: No duplicates
    nums5 = [1, 2, 3, 4, 5]
    k5 = sol.removeDuplicates(nums5)
    assert k5 == 5, f"Expected k=5, got k={k5}"
    assert nums5[:k5] == [1, 2, 3, 4, 5], f"Expected [1,2,3,4,5], got {nums5[:k5]}"
    print(f"✓ Test 5 passed: k={k5}, nums={nums5[:k5]}")

    # Test case 6: Two elements same
    nums6 = [1, 1]
    k6 = sol.removeDuplicates(nums6)
    assert k6 == 1, f"Expected k=1, got k={k6}"
    assert nums6[:k6] == [1], f"Expected [1], got {nums6[:k6]}"
    print(f"✓ Test 6 passed: k={k6}, nums={nums6[:k6]}")

    print("\n✅ All tests passed!")