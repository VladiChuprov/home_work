print("*" * 10, " Игра Крестики-нолики для двоих игроков с полем 3х3", "*" * 10)

field = list(range(1, 10))

def playing_field(field):
    print("-" * 13)
    for i in range(3):
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input(
            "Выберите номер ячейки, куда поставим " + player_token+"?\n ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(field[player_answer-1]) not in "XO"):
                field[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Номера ячеек от 1 до 9.")


def check_win(field):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def main(field):
    counter = 0
    win = False
    while not win:
        playing_field(field)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(field)
            if tmp:
                print(f'Выиграл игрок, играющий за {tmp}!')
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    playing_field(field)

main(field)
input("Нажмите Enter для выхода!")




