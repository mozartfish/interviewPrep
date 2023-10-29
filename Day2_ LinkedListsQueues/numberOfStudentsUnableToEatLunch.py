class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque 
        stuQ = deque(students)
        sandQ = deque(sandwiches)

        while stuQ and sandQ and sandQ[0] in stuQ:
            if sandQ[0] != stuQ[0]:
                student = stuQ.popleft()
                stuQ.append(student)
            else:
                stuQ.popleft()
                sandQ.popleft() 
        return len(stuQ)