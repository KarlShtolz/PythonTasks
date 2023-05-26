"""
Научитесь пользоваться стандартной структурой данных queue для целых чисел. Напишите программу, содержащую описание
очереди и моделирующую работу очереди, реализовав все указанные здесь методы.
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После
выполнения каждой команды программа должна вывести одну строчку.
Возможные команды для программы:
push n
Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.
pop
Удалить из очереди первый элемент. Программа должна вывести его значение.
front
Программа должна вывести значение первого элемента, не удаляя его из очереди.
size
Программа должна вывести количество элементов в очереди.
clear
Программа должна очистить очередь и вывести ok.
exit
Программа должна вывести bye и завершить работу.
Перед исполнением операций front и pop программа должна проверять, содержится ли в очереди хотя бы один элемент. Если
во входных данных встречается операция front или pop, и при этом очередь пуста, то программа должна вместо числового
значения вывести строку error.

INPUT:
push 3
push 14
size
clear
push 1
front
push 2
front
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
1
1
1
2
0
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
push 1
front
exit
OUTPUT:
ok
1
bye
"""

command = 0
index_first = 0
queue = []
while command != 'exit':
    command = input()
    if 'push' in command:
        if len(queue) - index_first <= index_first:
            queue = queue[index_first:]
            index_first = 0
        queue.append(int(command.split()[-1]))
        print('ok')
    elif command == 'pop':
        if len(queue) - index_first > 0:
            print(queue[index_first])
            index_first += 1
        else:
            print('error')
    elif command == 'front':
        print(queue[index_first]) if len(queue) - index_first > 0 else print('error')
    elif command == 'size':
        print(len(queue) - index_first)
    elif command == 'clear':
        queue = []
        index_first = 0
        print('ok')
    elif command == 'exit':
        print('bye')