"""
169. Majority Element
Difficulty: Easy
Date Solved: 2026-02-09
Link: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

Problem Description:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Approach:
- Use Boyer-Moore Voting Algorithm for O(n) time and O(1) space
- Maintain a candidate and count
- When count is 0, pick new candidate
- Increment count if element matches candidate, decrement otherwise
- Since majority element appears > n/2 times, it will always be the final candidate

Alternative approaches:
1. HashMap (O(n) time, O(n) space)
2. Sorting (O(n log n) time, O(1) space) - middle element is always majority

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Find the majority element using Boyer-Moore Voting Algorithm.
        """
        candidate = None
        count = 0

        # Find candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

    # Alternative solution using sorting
    def majorityElementSorting(self, nums: list[int]) -> int:
        """
        Find majority element by sorting.
        Middle element is always the majority element.
        """
        nums.sort()
        return nums[len(nums) // 2]

    # Alternative solution using HashMap
    def majorityElementHashMap(self, nums: list[int]) -> int:
        """
        Find majority element using HashMap to count occurrences.
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > len(nums) // 2:
                return num
        return -1


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [3, 2, 3]
    result1 = sol.majorityElement(nums1)
    assert result1 == 3, f"Expected 3, got {result1}"
    print(f"✓ Test 1 passed: {result1}")

    # Test case 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    result2 = sol.majorityElement(nums2)
    assert result2 == 2, f"Expected 2, got {result2}"
    print(f"✓ Test 2 passed: {result2}")

    # Test case 3: Single element
    nums3 = [1]
    result3 = sol.majorityElement(nums3)
    assert result3 == 1, f"Expected 1, got {result3}"
    print(f"✓ Test 3 passed: {result3}")

    # Test case 4: All same elements
    nums4 = [5, 5, 5, 5, 5]
    result4 = sol.majorityElement(nums4)
    assert result4 == 5, f"Expected 5, got {result4}"
    print(f"✓ Test 4 passed: {result4}")

    # Test case 5: Majority at the end
    nums5 = [1, 2, 3, 3, 3, 3, 3]
    result5 = sol.majorityElement(nums5)
    assert result5 == 3, f"Expected 3, got {result5}"
    print(f"✓ Test 5 passed: {result5}")

    # Test case 6: Two elements
    nums6 = [1, 1]
    result6 = sol.majorityElement(nums6)
    assert result6 == 1, f"Expected 1, got {result6}"
    print(f"✓ Test 6 passed: {result6}")

    # Test alternative solutions
    print("\n--- Testing alternative solutions ---")

    # Test sorting approach
    nums7 = [2, 2, 1, 1, 1, 2, 2]
    result7 = sol.majorityElementSorting(nums7)
    assert result7 == 2, f"Sorting: Expected 2, got {result7}"
    print(f"✓ Sorting approach passed: {result7}")

    # Test HashMap approach
    nums8 = [3, 2, 3]
    result8 = sol.majorityElementHashMap(nums8)
    assert result8 == 3, f"HashMap: Expected 3, got {result8}"
    print(f"✓ HashMap approach passed: {result8}")

    print("\n✅ All tests passed!")