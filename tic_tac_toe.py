# Создаем поле для игры
board = [[" "] * 3 for i in range(3)]


# Создаем функцию, показывающую доску
def show_board():
    print()
    print("    ║ 0 ║ 1 ║ 2 ║ ")
    print("  𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖 ")
    for i, row in enumerate(board):
        row_str = f"  {i} ║ {' ║ '.join(row)} ║ "
        print(row_str)
        print("  𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖𝄖 ")
    print()


# Создаем функцию для ввода данных пользователем
def input_analysis():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if board[x][y] != " ":
            print(" Выбранные координаты уже использованы! ")
            continue

        return x, y


# Создаем функцию для проверки результата игры
def game_check():
    win_combination = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                       ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                       ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))
                       )
    for combo in win_combination:
        line = []
        for c in combo:
            line.append(board[c[0]][c[1]])
        if line == ["X", "X", "X"]:
            print("Поздравляю, выиграл X!")
            return True
        if line == ["0", "0", "0"]:
            print("Поздравляю, выиграл 0!")
            return True
    return False


# Создаем цикл для самой игры, используя в нем созданные функции
def restart_game():
    print("Есть желание сыграть еще раз?")
    answer = input("Введи да или нет: ")
    if answer.lower() == 'да':
        greetings()
    elif answer.lower() == 'нет':
        print("Прощай!")
        quit()
    else:
        print("Ты ввел не то, что я просил :(")
        exit()


def start_game():
    move = 0
    while True:
        move += 1
        show_board()
        if move % 2 == 1:
            print(" Ходит крестик!")
        else:
            print(" Ходит нолик!")

        x, y = input_analysis()

        if move % 2 == 1:
            board[x][y] = "X"
        else:
            board[x][y] = "0"

        if game_check():
            break

        if move == 9:
            print("Ничья! Такое случается редко, но ты смог.")
            break
    restart_game()


# Создаем функцию приветствия и краткого описания игры.
def greetings():
    print("⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟ ")
    print(" Приветствую Вас в игре 'Крестики - нолики' ")
    print("⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟")
    print(" В данной игре тебе нужно будет вводить координаты x & y ")
    print("⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟")
    print(" Где 'x' - строка, а y - 'столбик' ")
    print("⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟")
    print(" Приятной вам игры! ")
    print(" Введите любую цифру, чтобы начать игру. ")
    User_response = input("☞: ")  # Добавил для возможности быстрого выхода, если нет желания играть
    if User_response.isdigit():
        start_game()
    else:
        print("До встречи!")


greetings()
