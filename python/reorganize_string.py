import heapq
from typing import Optional


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        NOTE: time complexity O(nlogn), space complexity O(n)
        1. Most frequent character should be placed first
        2. Use prev to store the previous character and skip it in the next iteration
        """
        counter: dict[str, int] = {}
        for c in s:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        max_heap: list[tuple[int, str]] = [
            (-1 * count, c) for c, count in counter.items()
        ]
        heapq.heapify(max_heap)
        result: str = ""
        prev: Optional[tuple[int, str]] = None
        while len(max_heap) > 0 or prev is not None:
            if len(max_heap) == 0 and prev is not None:
                return ""
            count, c = heapq.heappop(max_heap)
            result += c
            count += 1
            if prev is not None:
                heapq.heappush(max_heap, prev)
                prev = None
            if count < 0:
                prev = (count, c)
        return result


def test_reorganizeString_case_1():
    # arrange
    s: str = "aab"
    expected: str = "aba"

    # act
    solution = Solution()
    actual = solution.reorganizeString(s)

    # assert
    assert expected == actual


def test_reorganizeString_case_2():
    # arrange
    s: str = "aaab"
    expected: str = ""

    # act
    solution = Solution()
    actual = solution.reorganizeString(s)

    # assert
    assert expected == actual
