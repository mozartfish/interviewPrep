# runtime - O(n)
# space - constant since no additional space is allocated per element 
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = [] 
        for op in operations:
            if op == "+":
                if rec and len(rec) >= 2:
                    s1, s2 = rec[-1], rec[-2]
                    rec.append(s1 + s2)
                # pass 
            elif op == "D":
                if rec:
                    rec.append(2 * rec[-1])
                # pass 
            elif op == "C":
                rec.pop()
                # pass 
            else:
                rec.append(int(op))
        
        return sum(rec) # sum takes O(n) and loops through entire list 
        