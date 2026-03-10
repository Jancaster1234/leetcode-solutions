"""
122. Best Time to Buy and Sell Stock II
Difficulty: Medium
Date Solved: 2026-03-10
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

Problem Description:
You are given an integer array prices where prices[i] is the price of a given stock
on the ith day. On each day, you may decide to buy and/or sell the stock. You can
only hold at most one share of the stock at any time. However, you can sell and buy
the stock multiple times on the same day. Find and return the maximum profit you can achieve.

Approach:
- Greedy: capture every upward price movement
- If tomorrow's price is higher than today's, collect that profit
- This is equivalent to any optimal buy/sell strategy since transactions
  can occur on the same day
- Sum all positive differences between consecutive days

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Return maximum profit by capturing every upward price movement.
        """
        return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Two transactions
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = sol.maxProfit(prices1)
    assert result1 == 7, f"Expected 7, got {result1}"
    print(f"✓ Test 1 passed: profit={result1}")

    # Test case 2: One long transaction
    prices2 = [1, 2, 3, 4, 5]
    result2 = sol.maxProfit(prices2)
    assert result2 == 4, f"Expected 4, got {result2}"
    print(f"✓ Test 2 passed: profit={result2}")

    # Test case 3: Declining prices, no profit
    prices3 = [7, 6, 4, 3, 1]
    result3 = sol.maxProfit(prices3)
    assert result3 == 0, f"Expected 0, got {result3}"
    print(f"✓ Test 3 passed: profit={result3}")

    # Test case 4: Single day
    prices4 = [5]
    result4 = sol.maxProfit(prices4)
    assert result4 == 0, f"Expected 0, got {result4}"
    print(f"✓ Test 4 passed: profit={result4}")

    # Test case 5: Two days, profit
    prices5 = [1, 5]
    result5 = sol.maxProfit(prices5)
    assert result5 == 4, f"Expected 4, got {result5}"
    print(f"✓ Test 5 passed: profit={result5}")

    # Test case 6: Two days, no profit
    prices6 = [5, 1]
    result6 = sol.maxProfit(prices6)
    assert result6 == 0, f"Expected 0, got {result6}"
    print(f"✓ Test 6 passed: profit={result6}")

    # Test case 7: Flat prices
    prices7 = [3, 3, 3, 3]
    result7 = sol.maxProfit(prices7)
    assert result7 == 0, f"Expected 0, got {result7}"
    print(f"✓ Test 7 passed: profit={result7}")

    print("\n✅ All tests passed!")