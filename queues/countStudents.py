class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        '''
        - circle sandwiches represented by 0 
        - square sandwiches represented by 1 
        - number of sandwiches is equal to number of students 
        - all students stand in queue. each student prefers either a square OR a circle sandwich
        '''
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