class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        sandQ = deque(sandwiches)
        stuQ = deque(students)

        while sandQ and stuQ and sandQ[0] in stuQ:
            if sandQ[0] != stuQ[0]:
                student = stuQ.popleft() 
                stuQ.append(student)
            else:
                sandQ.popleft() 
                stuQ.popleft() 
        
        return len(stuQ)
        