class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = [] 
        for op in operations:
            if op == "D":
                top = rec[-1]
                rec.append(2 * top)
                # pass 
            elif op == "C":
                rec.pop()
                # pass 
            elif op == "+":
                if len(rec) >= 2:
                    rec1, rec2 = rec[-1], rec[-2]
                    rec.append(rec1 + rec2)
                # pass 
            else:
                rec.append(int(op))
        
        return sum(rec)