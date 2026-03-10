"""
121. Best Time to Buy and Sell Stock
Difficulty: Easy
Date Solved: 2026-03-10
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

Problem Description:
You are given an array prices where prices[i] is the price of a given stock on the
ith day. You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock. Return the maximum
profit you can achieve. If you cannot achieve any profit, return 0.

Approach:
- Track the minimum price seen so far as we iterate
- At each day, calculate profit if we sold today (price - min_price)
- Update max profit if current profit is better
- Single pass: no need to look back, min_price captures the best buy point so far

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Return maximum profit from a single buy and sell transaction.
        """
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Normal case with profit
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = sol.maxProfit(prices1)
    assert result1 == 5, f"Expected 5, got {result1}"
    print(f"✓ Test 1 passed: profit={result1}")

    # Test case 2: Declining prices, no profit
    prices2 = [7, 6, 4, 3, 1]
    result2 = sol.maxProfit(prices2)
    assert result2 == 0, f"Expected 0, got {result2}"
    print(f"✓ Test 2 passed: profit={result2}")

    # Test case 3: Single day
    prices3 = [5]
    result3 = sol.maxProfit(prices3)
    assert result3 == 0, f"Expected 0, got {result3}"
    print(f"✓ Test 3 passed: profit={result3}")

    # Test case 4: Two days, profit
    prices4 = [1, 5]
    result4 = sol.maxProfit(prices4)
    assert result4 == 4, f"Expected 4, got {result4}"
    print(f"✓ Test 4 passed: profit={result4}")

    # Test case 5: Two days, no profit
    prices5 = [5, 1]
    result5 = sol.maxProfit(prices5)
    assert result5 == 0, f"Expected 0, got {result5}"
    print(f"✓ Test 5 passed: profit={result5}")

    # Test case 6: Min at end, must not sell before buying
    prices6 = [6, 3, 7, 1]
    result6 = sol.maxProfit(prices6)
    assert result6 == 4, f"Expected 4, got {result6}"
    print(f"✓ Test 6 passed: profit={result6}")

    # Test case 7: All same prices
    prices7 = [3, 3, 3, 3]
    result7 = sol.maxProfit(prices7)
    assert result7 == 0, f"Expected 0, got {result7}"
    print(f"✓ Test 7 passed: profit={result7}")

    print("\n✅ All tests passed!")