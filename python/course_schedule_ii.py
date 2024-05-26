class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """time complexity: O(V + E) where V is the number of courses and E is the number of prerequisites"""
        result: list[int] = []
        course_graph: dict[int, list[int]] = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            course_graph[course].append(pre)
        visiting_set: set[int] = set()
        completed_set: set[int] = set()
        for c in range(numCourses):
            if self.dfs(c, result, course_graph, visiting_set, completed_set):
                continue
            return []
        return result

    def dfs(
        self,
        course: int,
        result: list[int],
        course_graph: dict[int, list[int]],
        visiting_set: set[int],
        completed_set: set[int],
    ) -> bool:
        if course in visiting_set:
            return False
        if course in completed_set:
            return True
        visiting_set.add(course)
        for pre in course_graph[course]:
            if self.dfs(pre, result, course_graph, visiting_set, completed_set):
                continue
            return False
        visiting_set.remove(course)
        completed_set.add(course)
        result.append(course)
        return True


def test_findOrder_case_1():
    # arrange
    numCourses: int = 2
    prerequisites: list[list[int]] = [[1, 0]]
    expected: list[int] = [0, 1]

    # act
    solution = Solution()
    actual: list[int] = solution.findOrder(numCourses, prerequisites)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_findOrder_case_2():
    # arrange
    numCourses: int = 4
    prerequisites: list[list[int]] = [[1, 0], [2, 0], [3, 1], [3, 2]]
    expected: list[int] = [0, 2, 1, 3]

    # act
    solution = Solution()
    actual: list[int] = solution.findOrder(numCourses, prerequisites)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_findOrder_case_3():
    # arrange
    numCourses: int = 1
    prerequisites: list[list[int]] = []
    expected: list[int] = [0]

    # act
    solution = Solution()
    actual: list[int] = solution.findOrder(numCourses, prerequisites)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
