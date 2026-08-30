class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for x in operations:
            if x not in ['C','D','+']:
                record.append(int(x))
            else:
                if x=="C":
                    record.pop(-1)
                elif x=="D":
                    record.append(int(record[-1]*2))
                else:
                    record.append(sum([record[-1],record[-2]]))
        return sum(record)