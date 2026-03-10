"""
55. Jump Game
Difficulty: Medium
Date Solved: 2026-03-10
Link: https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

Problem Description:
You are given an integer array nums. You are initially positioned at the array's
first index, and each element in the array represents your maximum jump length at
that position. Return true if you can reach the last index, or false otherwise.

Approach:
- Greedy: track the farthest index reachable at any point
- Iterate through each index up to the current max reach
- At each index, update max_reach = max(max_reach, i + nums[i])
- If max_reach >= last index at any point, return True
- If we ever reach an index beyond max_reach, we're stuck — return False

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Return True if the last index is reachable from index 0.
        """
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Can reach end
    nums1 = [2, 3, 1, 1, 4]
    result1 = sol.canJump(nums1)
    assert result1 == True, f"Expected True, got {result1}"
    print(f"✓ Test 1 passed: {result1}")

    # Test case 2: Stuck at zero, cannot reach end
    nums2 = [3, 2, 1, 0, 4]
    result2 = sol.canJump(nums2)
    assert result2 == False, f"Expected False, got {result2}"
    print(f"✓ Test 2 passed: {result2}")

    # Test case 3: Single element, already at last index
    nums3 = [0]
    result3 = sol.canJump(nums3)
    assert result3 == True, f"Expected True, got {result3}"
    print(f"✓ Test 3 passed: {result3}")

    # Test case 4: Two elements, can jump
    nums4 = [1, 0]
    result4 = sol.canJump(nums4)
    assert result4 == True, f"Expected True, got {result4}"
    print(f"✓ Test 4 passed: {result4}")

    # Test case 5: Two elements, cannot jump
    nums5 = [0, 1]
    result5 = sol.canJump(nums5)
    assert result5 == False, f"Expected False, got {result5}"
    print(f"✓ Test 5 passed: {result5}")

    # Test case 6: Large jump from start clears everything
    nums6 = [5, 0, 0, 0, 0]
    result6 = sol.canJump(nums6)
    assert result6 == True, f"Expected True, got {result6}"
    print(f"✓ Test 6 passed: {result6}")

    # Test case 7: Zero in the middle blocks path
    nums7 = [1, 0, 1, 1, 1]
    result7 = sol.canJump(nums7)
    assert result7 == False, f"Expected False, got {result7}"
    print(f"✓ Test 7 passed: {result7}")

    # Test case 8: All ones
    nums8 = [1, 1, 1, 1, 1]
    result8 = sol.canJump(nums8)
    assert result8 == True, f"Expected True, got {result8}"
    print(f"✓ Test 8 passed: {result8}")

    print("\n✅ All tests passed!")