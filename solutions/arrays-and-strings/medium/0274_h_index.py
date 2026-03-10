"""
274. H-Index
Difficulty: Medium
Date Solved: 2026-03-10
Link: https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

Problem Description:
Given an array of integers citations where citations[i] is the number of citations
a researcher received for their ith paper, return the researcher's h-index.
The h-index is the maximum value h such that the researcher has at least h papers
that have each been cited at least h times.

Approach:
- Sort citations in descending order
- Iterate through sorted list: at index i, there are (i+1) papers with >= citations[i] citations
- h-index is the largest i+1 where citations[i] >= i+1
- As soon as citations[i] < i+1, we've gone too far — return i

Time Complexity: O(n log n)
Space Complexity: O(1)
"""


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        Return the h-index of a researcher given their citation counts.
        """
        citations.sort(reverse=True)

        for i, c in enumerate(citations):
            if c < i + 1:
                return i

        return len(citations)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Standard case
    citations1 = [3, 0, 6, 1, 5]
    result1 = sol.hIndex(citations1)
    assert result1 == 3, f"Expected 3, got {result1}"
    print(f"✓ Test 1 passed: h-index={result1}")

    # Test case 2: Small case
    citations2 = [1, 3, 1]
    result2 = sol.hIndex(citations2)
    assert result2 == 1, f"Expected 1, got {result2}"
    print(f"✓ Test 2 passed: h-index={result2}")

    # Test case 3: All zeros, no citations
    citations3 = [0, 0, 0]
    result3 = sol.hIndex(citations3)
    assert result3 == 0, f"Expected 0, got {result3}"
    print(f"✓ Test 3 passed: h-index={result3}")

    # Test case 4: Single paper with citations
    citations4 = [5]
    result4 = sol.hIndex(citations4)
    assert result4 == 1, f"Expected 1, got {result4}"
    print(f"✓ Test 4 passed: h-index={result4}")

    # Test case 5: Single paper with zero citations
    citations5 = [0]
    result5 = sol.hIndex(citations5)
    assert result5 == 0, f"Expected 0, got {result5}"
    print(f"✓ Test 5 passed: h-index={result5}")

    # Test case 6: All papers have same high citation count
    citations6 = [4, 4, 4, 4]
    result6 = sol.hIndex(citations6)
    assert result6 == 4, f"Expected 4, got {result6}"
    print(f"✓ Test 6 passed: h-index={result6}")

    # Test case 7: h-index capped by number of papers
    citations7 = [100, 100, 100]
    result7 = sol.hIndex(citations7)
    assert result7 == 3, f"Expected 3, got {result7}"
    print(f"✓ Test 7 passed: h-index={result7}")

    # Test case 8: Strictly decreasing
    citations8 = [5, 4, 3, 2, 1]
    result8 = sol.hIndex(citations8)
    assert result8 == 3, f"Expected 3, got {result8}"
    print(f"✓ Test 8 passed: h-index={result8}")

    print("\n✅ All tests passed!")