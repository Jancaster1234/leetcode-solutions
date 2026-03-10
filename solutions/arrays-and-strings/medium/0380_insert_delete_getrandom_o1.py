"""
380. Insert Delete GetRandom O(1)
Difficulty: Medium
Date Solved: 2026-03-10
Link: https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150

Problem Description:
Implement a RandomizedSet class that supports insert, remove, and getRandom,
all in average O(1) time complexity.

Approach:
- Use a list for O(1) random access (getRandom) and a dict for O(1) lookup
- dict maps val -> index in list
- insert: append to list, store index in dict
- remove: swap target with last element, update dict, pop from list
  - Swapping avoids O(n) shift; only the swapped element's index needs updating
- getRandom: return random.choice(list)

Time Complexity: O(1) average for all operations
Space Complexity: O(n)
"""

import random


class RandomizedSet:
    def __init__(self):
        self.val_to_idx = {}  # val -> index in list
        self.vals = []        # list of values for O(1) random access

    def insert(self, val: int) -> bool:
        """Insert val if not present. Returns True if inserted, False if already exists."""
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        """Remove val if present. Returns True if removed, False if not found."""
        if val not in self.val_to_idx:
            return False
        # Swap with last element to avoid O(n) deletion
        idx = self.val_to_idx[val]
        last = self.vals[-1]
        self.vals[idx] = last
        self.val_to_idx[last] = idx
        # Remove last element
        self.vals.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        """Return a random element from the set with equal probability."""
        return random.choice(self.vals)


# Test cases
if __name__ == "__main__":
    # Test case 1: Example from problem
    rs = RandomizedSet()
    assert rs.insert(1) == True,  "Expected True"
    assert rs.remove(2) == False, "Expected False"
    assert rs.insert(2) == True,  "Expected True"
    assert rs.getRandom() in [1, 2], "Expected 1 or 2"
    assert rs.remove(1) == True,  "Expected True"
    assert rs.insert(2) == False, "Expected False"
    assert rs.getRandom() == 2,   "Expected 2"
    print("✓ Test 1 passed: example case")

    # Test case 2: Insert duplicates
    rs2 = RandomizedSet()
    assert rs2.insert(10) == True,  "Expected True"
    assert rs2.insert(10) == False, "Expected False (duplicate)"
    print("✓ Test 2 passed: duplicate insert")

    # Test case 3: Remove non-existent
    rs3 = RandomizedSet()
    assert rs3.remove(99) == False, "Expected False (not present)"
    print("✓ Test 3 passed: remove non-existent")

    # Test case 4: Single element getRandom
    rs4 = RandomizedSet()
    rs4.insert(42)
    assert rs4.getRandom() == 42, "Expected 42"
    print("✓ Test 4 passed: single element getRandom")

    # Test case 5: Remove last element after swap
    rs5 = RandomizedSet()
    rs5.insert(1)
    rs5.insert(2)
    rs5.insert(3)
    assert rs5.remove(1) == True, "Expected True"
    assert rs5.getRandom() in [2, 3], "Expected 2 or 3"
    print("✓ Test 5 passed: remove and swap correctness")

    # Test case 6: getRandom distribution is uniform
    rs6 = RandomizedSet()
    rs6.insert(1)
    rs6.insert(2)
    results = [rs6.getRandom() for _ in range(1000)]
    count_1 = results.count(1)
    count_2 = results.count(2)
    assert 350 < count_1 < 650, f"Distribution skewed: 1 appeared {count_1}/1000 times"
    assert 350 < count_2 < 650, f"Distribution skewed: 2 appeared {count_2}/1000 times"
    print(f"✓ Test 6 passed: uniform distribution (1:{count_1}, 2:{count_2} over 1000 samples)")

    # Test case 7: Full insert/remove/reinsert cycle
    rs7 = RandomizedSet()
    assert rs7.insert(5) == True,  "Expected True"
    assert rs7.remove(5) == True,  "Expected True"
    assert rs7.insert(5) == True,  "Expected True (reinsert after remove)"
    assert rs7.getRandom() == 5,   "Expected 5"
    print("✓ Test 7 passed: insert -> remove -> reinsert cycle")

    print("\n✅ All tests passed!")