"""
27. Remove Element
Difficulty: Easy
Date Solved: 2026-02-09
Link: https://leetcode.com/problems/remove-element?envType=study-plan-v2&envId=top-interview-150

Problem Description:
Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Then return the
number of elements in nums which are not equal to val.

Approach:
- Use two pointers technique
- Left pointer (k) tracks position to place non-val elements
- Right pointer iterates through array
- When we find a non-val element, place it at position k and increment k
- Return k as the count of elements not equal to val

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Remove all occurrences of val in-place and return new length.
        """
        k = 0  # pointer for placing non-val elements

        # Iterate through the array
        for i in range(len(nums)):
            # If current element is not val, keep it
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [3, 2, 2, 3]
    k1 = sol.removeElement(nums1, 3)
    assert k1 == 2, f"Expected k=2, got k={k1}"
    assert sorted(nums1[:k1]) == [2, 2], f"Expected [2,2], got {sorted(nums1[:k1])}"
    print(f"✓ Test 1 passed: k={k1}, nums={nums1[:k1]}")

    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    k2 = sol.removeElement(nums2, 2)
    assert k2 == 5, f"Expected k=5, got k={k2}"
    assert sorted(nums2[:k2]) == [0, 0, 1, 3, 4], f"Expected [0,0,1,3,4], got {sorted(nums2[:k2])}"
    print(f"✓ Test 2 passed: k={k2}, nums={sorted(nums2[:k2])}")

    # Test case 3: Empty array
    nums3 = []
    k3 = sol.removeElement(nums3, 1)
    assert k3 == 0, f"Expected k=0, got k={k3}"
    print(f"✓ Test 3 passed: k={k3}, nums={nums3[:k3]}")

    # Test case 4: All elements are val
    nums4 = [1, 1, 1, 1]
    k4 = sol.removeElement(nums4, 1)
    assert k4 == 0, f"Expected k=0, got k={k4}"
    print(f"✓ Test 4 passed: k={k4}, nums={nums4[:k4]}")

    # Test case 5: No elements equal val
    nums5 = [1, 2, 3, 4]
    k5 = sol.removeElement(nums5, 5)
    assert k5 == 4, f"Expected k=4, got k={k5}"
    assert nums5[:k5] == [1, 2, 3, 4], f"Expected [1,2,3,4], got {nums5[:k5]}"
    print(f"✓ Test 5 passed: k={k5}, nums={nums5[:k5]}")

    print("\n✅ All tests passed!")