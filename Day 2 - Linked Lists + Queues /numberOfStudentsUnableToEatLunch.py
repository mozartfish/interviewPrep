# runtime - O(n) where n represents the length of the number of students left 
# space time - constant no additional space added per element 
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque 
        sandQ = deque(sandwiches)
        stuQ = deque(students)

        while stuQ and sandQ and sandQ[0] in stuQ:
            if sandQ[0] != stuQ[0]:
                student = stuQ.popleft() 
                stuQ.append(student)
            else:
                stuQ.popleft() 
                sandQ.popleft() 
        
        return len(stuQ)

        