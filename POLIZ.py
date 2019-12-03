import operator

def calc(expr):

    OPERATORS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
        }

    mystack = []                                              # Задаємо нульовий список

    for token in expr.split(" "):                             # Розбиває строку expr по роздільнику "пробілу"
        if token in OPERATORS:
            op2, op1 = mystack.pop(), mystack.pop()
            mystack.append(OPERATORS[token](op1,op2))

        elif token:
            mystack.append(float(token))

        return stack.pop()

def main():
        expr = '2 + 3'
        print(calc(expr))

if __name__ == "__main__":
        main()


