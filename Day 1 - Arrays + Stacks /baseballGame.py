class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == "+":
                if len(record) > 1:
                    s1, s2 = record[-1], record[-2]
                    record.append(s1 + s2)
                # pass 
            elif operation == "D":
                if record:
                    record.append(2 * record[-1])
                # pass 
            elif operation == "C":
                record.pop()
                # pass 
            else:
                record.append(int(operation))
        
        return sum(record)