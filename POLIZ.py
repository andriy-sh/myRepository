import operator
expr = '3 4 5 * + 7 + 4 6 - /'


mystack = []
def calc():
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    for token in expr.split(" "):
        if token in OPERATORS:
            mystack.append(OPERATORS[token](op1,op2))
        elif token:
            mystack.append(float(token))
    return stack.pop()
    print(stack.pop())

calc('3 4 5 * + 7 + 4 6 - /')
