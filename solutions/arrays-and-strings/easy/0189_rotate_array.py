"""
189. Rotate Array
Difficulty: Medium
Date Solved: 2026-02-09
Link: https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

Problem Description:
Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

Approach (Reverse Method - Optimal):
- Use three reverse operations to achieve rotation in O(1) space
- Step 1: Reverse entire array
- Step 2: Reverse first k elements
- Step 3: Reverse remaining n-k elements
- Handle k > n by taking k % n

Example: nums=[1,2,3,4,5,6,7], k=3
1. Reverse all: [7,6,5,4,3,2,1]
2. Reverse first 3: [5,6,7,4,3,2,1]
3. Reverse last 4: [5,6,7,1,2,3,4] ✓

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotate array in-place using reverse method.
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle k > n

        # Helper function to reverse a portion of the array
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Three-step reverse
        reverse(0, n - 1)  # Reverse entire array
        reverse(0, k - 1)  # Reverse first k elements
        reverse(k, n - 1)  # Reverse remaining elements

    # Alternative solution using extra space
    def rotateExtraSpace(self, nums: list[int], k: int) -> None:
        """
        Rotate using extra array (O(n) space).
        """
        n = len(nums)
        k = k % n
        rotated = nums[-k:] + nums[:-k]
        nums[:] = rotated

    # Alternative solution using cyclic replacements
    def rotateCyclic(self, nums: list[int], k: int) -> None:
        """
        Rotate using cyclic replacements (O(1) space, more complex).
        """
        n = len(nums)
        k = k % n
        count = 0

        start = 0
        while count < n:
            current = start
            prev = nums[start]

            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break

            start += 1


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums1, 3)
    assert nums1 == [5, 6, 7, 1, 2, 3, 4], f"Expected [5,6,7,1,2,3,4], got {nums1}"
    print(f"✓ Test 1 passed: {nums1}")

    # Test case 2
    nums2 = [-1, -100, 3, 99]
    sol.rotate(nums2, 2)
    assert nums2 == [3, 99, -1, -100], f"Expected [3,99,-1,-100], got {nums2}"
    print(f"✓ Test 2 passed: {nums2}")

    # Test case 3: k = 0
    nums3 = [1, 2, 3]
    sol.rotate(nums3, 0)
    assert nums3 == [1, 2, 3], f"Expected [1,2,3], got {nums3}"
    print(f"✓ Test 3 passed: {nums3}")

    # Test case 4: k > n
    nums4 = [1, 2, 3, 4, 5]
    sol.rotate(nums4, 7)  # Same as k=2
    assert nums4 == [4, 5, 1, 2, 3], f"Expected [4,5,1,2,3], got {nums4}"
    print(f"✓ Test 4 passed: {nums4}")

    # Test case 5: Single element
    nums5 = [1]
    sol.rotate(nums5, 3)
    assert nums5 == [1], f"Expected [1], got {nums5}"
    print(f"✓ Test 5 passed: {nums5}")

    # Test case 6: k = n (full rotation)
    nums6 = [1, 2, 3, 4]
    sol.rotate(nums6, 4)
    assert nums6 == [1, 2, 3, 4], f"Expected [1,2,3,4], got {nums6}"
    print(f"✓ Test 6 passed: {nums6}")

    # Test case 7: Two elements
    nums7 = [1, 2]
    sol.rotate(nums7, 1)
    assert nums7 == [2, 1], f"Expected [2,1], got {nums7}"
    print(f"✓ Test 7 passed: {nums7}")

    # Test alternative solution (extra space)
    print("\n--- Testing extra space solution ---")
    nums8 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotateExtraSpace(nums8, 3)
    assert nums8 == [5, 6, 7, 1, 2, 3, 4], f"Expected [5,6,7,1,2,3,4], got {nums8}"
    print(f"✓ Extra space solution passed: {nums8}")

    # Test cyclic replacement solution
    print("\n--- Testing cyclic replacement solution ---")
    nums9 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotateCyclic(nums9, 3)
    assert nums9 == [5, 6, 7, 1, 2, 3, 4], f"Expected [5,6,7,1,2,3,4], got {nums9}"
    print(f"✓ Cyclic replacement solution passed: {nums9}")

    print("\n✅ All tests passed!")