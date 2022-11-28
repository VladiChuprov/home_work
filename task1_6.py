

num = list(range(1,10))

def print_coub(num):
    print ('-'*13)
    for i in range(3):
        print(f'| {num[0+3*i]} | {num[1+ i*3]} | {num[2+i*3]} |')
        print ('-'*13)


def player_move(player_action):
    valid = False
    while not valid:
        player_number = input( "Укажите ячейку куда поставите  "+player_action+ ' ?  ')
        try:
             player_number =int(player_number)
        except:
            print("введите число ")
            continue
        if 1<=player_number<=9 :
            if str(num[player_number-1]) not in 'XO':
                num[player_number-1]=player_action
                valid = True
            else :
                print('Клетка занята')
        else:
            print("Введите номер ячейки от 1 до 9")



def win_line(num):
    win_number =(((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)))
    for each in win_number:
        if num[each[0]]==num[each[1]]==num[each[2]]:
            return num[each[0]]
    return False

def main(num):
    count =0
    win=False
    while not win:
        print_coub(num)
        if count%2 !=0:
            player_move('O')
            player_move('X')
        count+=1
        if count > 4:
           tmp = win_line(num)
           if tmp:            
              print(f'Выиграл игрок, играющий за "{tmp}"!')              
              win = True
              break
        if count == 9:                  
            print('Ничья!')
            break
    print_coub(num)


main(num)

input("Нажмите Enter для выхода!")




