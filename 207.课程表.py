from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        self.course_graph = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            self.course_graph[course].append(pre)


        # now it turns to a dfs problem

        self.already_studied = set()
        for course in range(0, numCourses):

            pending = set()
            try:
                self.start_learning(course, pending)
            except Exception:
                return False

        return True

    def start_learning(self, current_course, pending_study):

        if current_course in self.already_studied:
            return

        if current_course in pending_study:
            raise Exception("Cant study the pending course")


        for pre in self.course_graph[current_course]:
            # need to study pre first
            pending_study.add(current_course)
            self.start_learning(pre, pending_study)
            pending_study.remove(current_course)

        self.already_studied.add(current_course)
            

if __name__ == "__main__":
    numCourses = 2
    # prerequisites = [[1,0],[0,1]]
    # prerequisites = [[1,0]]
    prerequisites = [[0,1]]

    s = Solution()
    res = s.canFinish(numCourses, prerequisites)

    print(res)

            


