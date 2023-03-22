def greetings():
    print("-------------------")
    print("  Добро пожаловать ")
    print("       в игру      ")
    print("  Крестики-Нолики  ")
    print("-------------------")
    print("     Управление:   ")
    print(" х - номер строки  ")
    print(" y - номер столбца ")

def cells():
    print()
    print("   | 0 | 1 | 2 | ")
    print(" --------------- ")
    for i, row in enumerate (field):
        row_str = f" {i} | { ' | '.join(row)} | "
        print(row_str)
        print(" --------------- ")
    print()


def coordinates():
    while True:
        cords = input("     Ваш ход: ").split()

        if len(cords) != 2:
            print(" ВВедите 2 координаты ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x , y


def winner():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbol = []
        for c in cord:
            symbol.append(field[c[0]][c[1]])
        if symbol == ["X", "X", "X"]:
            print(" Выиграл Х! ")
            return True
        if symbol == ["O", "O", "O"]:
            print(" Выиграл О! ")
            return True
    return False


greetings()
field = [[' '] * 3 for i in range(3) ]
num = 0
while True:
    num += 1
    cells()
    if num % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")

    x, y = coordinates()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if winner():
        break

    if num == 9:
        print(" Ничья ")
        break