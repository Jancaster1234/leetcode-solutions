"""
45. Jump Game II
Difficulty: Medium
Date Solved: 2026-03-10
Link: https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150

Problem Description:
You are given a 0-indexed array of integers nums of length n. You are initially
positioned at index 0. Each element nums[i] represents the maximum length of a
forward jump from index i. Return the minimum number of jumps to reach index n-1.

Approach:
- Greedy: treat each jump as covering a "window" of reachable indices
- Track current window end (cur_end) and farthest reach within that window (max_reach)
- When we exhaust the current window (i == cur_end), we must take a jump
- The next window extends to max_reach — the best we could reach from any index
  in the previous window
- Stop before the last index to avoid counting an unnecessary extra jump

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        Return the minimum number of jumps to reach the last index.
        """
        jumps = 0
        cur_end = 0
        max_reach = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = max_reach

        return jumps


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Classic two-jump case
    nums1 = [2, 3, 1, 1, 4]
    result1 = sol.jump(nums1)
    assert result1 == 2, f"Expected 2, got {result1}"
    print(f"✓ Test 1 passed: jumps={result1}")

    # Test case 2: Zero in middle, still reachable
    nums2 = [2, 3, 0, 1, 4]
    result2 = sol.jump(nums2)
    assert result2 == 2, f"Expected 2, got {result2}"
    print(f"✓ Test 2 passed: jumps={result2}")

    # Test case 3: Single element, already at destination
    nums3 = [0]
    result3 = sol.jump(nums3)
    assert result3 == 0, f"Expected 0, got {result3}"
    print(f"✓ Test 3 passed: jumps={result3}")

    # Test case 4: Two elements, one jump needed
    nums4 = [1, 0]
    result4 = sol.jump(nums4)
    assert result4 == 1, f"Expected 1, got {result4}"
    print(f"✓ Test 4 passed: jumps={result4}")

    # Test case 5: Large jump from start clears everything
    nums5 = [5, 0, 0, 0, 0]
    result5 = sol.jump(nums5)
    assert result5 == 1, f"Expected 1, got {result5}"
    print(f"✓ Test 5 passed: jumps={result5}")

    # Test case 6: All ones, must jump every step
    nums6 = [1, 1, 1, 1, 1]
    result6 = sol.jump(nums6)
    assert result6 == 4, f"Expected 4, got {result6}"
    print(f"✓ Test 6 passed: jumps={result6}")

    # Test case 7: Greedy must pick best window, not just first jump
    nums7 = [1, 2, 3, 4, 5]
    result7 = sol.jump(nums7)
    assert result7 == 3, f"Expected 3, got {result7}"
    print(f"✓ Test 7 passed: jumps={result7}")

    # Test case 8: Two elements with large jump value
    nums8 = [10, 0]
    result8 = sol.jump(nums8)
    assert result8 == 1, f"Expected 1, got {result8}"
    print(f"✓ Test 8 passed: jumps={result8}")

    print("\n✅ All tests passed!")