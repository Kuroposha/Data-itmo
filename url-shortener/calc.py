from collections import deque, namedtuple
import operator
from io import StringIO
import tokenize

LEFT_ASSOC = -1
RIGHT_ASSOC = 1

Operator = namedtuple('Operator',
                      ('assoc', 'prior', 'funk'))
OPER = {
    '+': Operator(LEFT_ASSOC, 10, operator.add),
    '-': Operator(LEFT_ASSOC, 10, operator.sub),
    '*': Operator(LEFT_ASSOC, 11, operator.mul),
    '/': Operator(LEFT_ASSOC, 11, operator.truediv),
    '^': Operator(RIGHT_ASSOC, 13, operator.pow)
}


def convert(expr):
    rpn = deque()
    stack = deque()

    for token in tokenize.generate_tokens(StringIO(expr).readline):
        token_type, value, *_ = token
        # звезда используется в левой части опер присв(последний эл-т
        # и забирает себе все остальное в кортеж)

        if token_type == tokenize.NUMBER:
            rpn.append(value)
        elif token_type == tokenize.OP:
            if value == '(':
                stack.append(value)
            elif token_type == ')':# нужна обработка ошибок
                while stack:top = stack.pop()

                if top == '(':
                    break

                rpn.append(top)
            else:# нужна проверка на ошибки
                oper_info = OPER.get(value)
                flag = True

                while stack and stack[-1] != '(' and flag:
                    top_oper = stack[-1]
                    top_oper_info = OPER.get(top_oper)

                    flag = (oper_info.assoc == RIGHT_ASSOC and oper_info.prior < top_oper_info.prior)\
                           or\
                           (oper_info.prior <= top_oper_info.prior)

                    if flag:
                        rpn.append(stack.pop())

                stack.append(value)

        while stack:
            rpn.append(stack.pop())

        return ' '.join(rpn)

#



def calc(expr):
    rpn = convert(expr)
    stack = deque()

    for token in rpn.split(' '):
        if token in OPER:
            op2, op1 = stack.pop(), stack.pop()
            oper = OPER.get(token)
            stack.append(oper.funk(op1, op2))
        else:
            stack.append(float(token))

    return stack.pop()

if __name__ == '__main__':
    #expr = input()
    expr = '3 + 4 * 2 / (1 - 5) ^ 2' # 3.5
    print(calc(expr))
