"""
Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа дожна определить,
 является ли данная скобочная последовательность правильной. Пустая последовательность явлется правильной.
 Если A – правильная, то последовательности (A), [A], {A} – правильные. Если A и B – правильные последовательности,
 то последовательность AB – правильная.
INPUT:
([)]
OUTPUT:
no
INPUT:
()[]
OUTPUT:
yes
"""
s = input()
def isValid(s: str) -> str:

    yes = "yes"
    no = "no"
    leftSymbols = []
    for c in s:
        if c in ['(', '{', '[']:
            leftSymbols.append(c)
        elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
            leftSymbols.pop()
        elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
            leftSymbols.pop()
        elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
            leftSymbols.pop()
        else:
            print(no)
            return no
    if leftSymbols == []:
        print(yes)
        return yes
    else:
        print(no)
        return no
isValid(s)