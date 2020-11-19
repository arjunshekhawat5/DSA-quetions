class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        graph = {}

        for i in pre:
            if i[0] not in graph:
                graph[i[0]] = []
            graph[i].append(i[1])

        print(graph)
