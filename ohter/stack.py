"""
Научитесь пользоваться стандартной структурой данных stack для целых чисел. Напишите программу,
содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы.
Программа считывает последовательность команд и в зависимости от команды выполняет ту или
иную операцию. После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:
push n
Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.
pop
Удалить из стека последний элемент. Программа должна вывести его значение.
back
Программа должна вывести значение последнего элемента, не удаляя его из стека.
size
Программа должна вывести количество элементов в стеке.
clear
Программа должна очистить стек и вывести ok.
exit
Программа должна вывести bye и завершить работу.
Перед исполнением операций back и pop программа должна проверять, содержится ли в стеке хотя
бы один элемент. Если во входных данных встречается операция back или pop, и при этом стек пуст,
то программа должна вместо числового значения вывести строку error.

INPUT:
push 1
back
exit
OUTPUT:
ok
1
bye

INPUT:
size
push 1
size
push 2
size
push 3
size
exit
OUTPUT:
0
ok
1
ok
2
ok
3
bye

INPUT:
push 3
push 14
size
clear
push 1
back
push 2
back
pop
size
pop
size
exit
OUTPUT:
ok
ok
2
ok
ok
1
ok
2
2
1
1
0
bye

"""

res = []
stack = []
while True:
    command, *args = input().split()
    if command == "size":
        res.append(len(stack))
    elif command == "back":
      if len(stack) == 0:
        res.append('error')
      else:
        res.append(stack[-1])
    elif command == "pop":
      if len(stack) == 0:
        res.append('error')
      else:
        res.append(stack.pop())
    elif command == "clear":
        stack.clear()
        res.append("ok")
    elif command == "push":
        stack.append(int(args[0]))
        res.append("ok")
    elif command == "exit":
        res.append("bye")
        break
print(*res, sep='\n')