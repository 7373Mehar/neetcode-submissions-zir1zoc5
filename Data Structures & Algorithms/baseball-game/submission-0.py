class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for i in range(len(operations)):
            if operations[i].isnumeric() or self.check_int(operations[i]):
                intOp = int(operations[i])
                res.append(intOp)
            
            elif operations[i] == 'D':
                doubleScore = 2 * res[-1]
                res.append(doubleScore)

            elif operations[i] == 'C':
                res.pop()

            elif operations[i] == '+':
                sumOp = res[-1] + res[-2]
                res.append(sumOp)

        return sum(res) 
    
    def check_int(self, s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()