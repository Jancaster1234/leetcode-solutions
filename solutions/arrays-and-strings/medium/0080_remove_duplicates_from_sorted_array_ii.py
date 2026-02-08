"""
80. Remove Duplicates from Sorted Array II
Difficulty: Medium
Date Solved: 2026-02-09
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

Problem Description:
Given an integer array nums sorted in non-decreasing order, remove some duplicates
in-place such that each unique element appears at most twice. The relative order
of the elements should be kept the same.

Approach:
- Use two pointers technique
- Pointer k tracks position for next valid element
- We can always keep first 2 elements (they can't exceed "at most twice")
- For i >= 2, only add nums[i] if it's different from nums[k-2]
- This ensures we never have more than 2 consecutive duplicates
- Works because array is sorted (duplicates are adjacent)

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Remove duplicates in-place, keeping at most 2 of each element.
        """
        if len(nums) <= 2:
            return len(nums)

        k = 2  # First two elements are always valid

        # Start checking from index 2
        for i in range(2, len(nums)):
            # Only add if different from element 2 positions back
            # This ensures at most 2 duplicates
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = sol.removeDuplicates(nums1)
    assert k1 == 5, f"Expected k=5, got k={k1}"
    assert nums1[:k1] == [1, 1, 2, 2, 3], f"Expected [1,1,2,2,3], got {nums1[:k1]}"
    print(f"✓ Test 1 passed: k={k1}, nums={nums1[:k1]}")

    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k2 = sol.removeDuplicates(nums2)
    assert k2 == 7, f"Expected k=7, got k={k2}"
    assert nums2[:k2] == [0, 0, 1, 1, 2, 3, 3], f"Expected [0,0,1,1,2,3,3], got {nums2[:k2]}"
    print(f"✓ Test 2 passed: k={k2}, nums={nums2[:k2]}")

    # Test case 3: Single element
    nums3 = [1]
    k3 = sol.removeDuplicates(nums3)
    assert k3 == 1, f"Expected k=1, got k={k3}"
    assert nums3[:k3] == [1], f"Expected [1], got {nums3[:k3]}"
    print(f"✓ Test 3 passed: k={k3}, nums={nums3[:k3]}")

    # Test case 4: Two elements same
    nums4 = [1, 1]
    k4 = sol.removeDuplicates(nums4)
    assert k4 == 2, f"Expected k=2, got k={k4}"
    assert nums4[:k4] == [1, 1], f"Expected [1,1], got {nums4[:k4]}"
    print(f"✓ Test 4 passed: k={k4}, nums={nums4[:k4]}")

    # Test case 5: All same elements
    nums5 = [1, 1, 1, 1, 1]
    k5 = sol.removeDuplicates(nums5)
    assert k5 == 2, f"Expected k=2, got k={k5}"
    assert nums5[:k5] == [1, 1], f"Expected [1,1], got {nums5[:k5]}"
    print(f"✓ Test 5 passed: k={k5}, nums={nums5[:k5]}")

    # Test case 6: No duplicates
    nums6 = [1, 2, 3, 4, 5]
    k6 = sol.removeDuplicates(nums6)
    assert k6 == 5, f"Expected k=5, got k={k6}"
    assert nums6[:k6] == [1, 2, 3, 4, 5], f"Expected [1,2,3,4,5], got {nums6[:k6]}"
    print(f"✓ Test 6 passed: k={k6}, nums={nums6[:k6]}")

    # Test case 7: Exactly 2 of each
    nums7 = [1, 1, 2, 2, 3, 3]
    k7 = sol.removeDuplicates(nums7)
    assert k7 == 6, f"Expected k=6, got k={k7}"
    assert nums7[:k7] == [1, 1, 2, 2, 3, 3], f"Expected [1,1,2,2,3,3], got {nums7[:k7]}"
    print(f"✓ Test 7 passed: k={k7}, nums={nums7[:k7]}")

    print("\n✅ All tests passed!")