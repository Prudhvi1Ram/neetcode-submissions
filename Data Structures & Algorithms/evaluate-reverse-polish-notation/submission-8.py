class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=[]
        symbol=["+","*","-","/"]
        for i in range(len(tokens)):
            if tokens[i] not in symbol:
                res.append(tokens[i])
            elif tokens[i] in symbol:
                op=tokens[i]
                a1=int(res[-1])
                res.pop()
                a2=int(res[-1])
                res.pop()
                if op == "+":
                    res.append(a2+a1)
                elif op == "-":
                    res.append(a2-a1)
                elif op == "*":
                    res.append(a2*a1)
                elif op == "/":
                    res.append(int(a2/a1))
        if len(tokens) == 1:
            return int(tokens[0])
        else:
            return (res[0])


        