

game_field = {0 : ['-', '-', '-'], 1 : ['-', '-', '-'], 2: ['-', '-', '-']}
field_numbers = [0, 1, 2]  
move_counter = 0   

def show_game_field(field: dict[int,list[str]]) -> None:
    
    print()
    print("  0 1 2")
    for key, value in field.items():
        print(f"{key} {' '.join(value)}")
    print()

def game_over(field: dict[int,list[str]]) -> bool:
    
    X = ['X', 'X', 'X']     
    O = ['O', 'O', 'O']     
    C0, C1, C2, D00_22, D02_20 = [], [], [], [], []     
    for key, value in field.items():
        if value == O or value == X:       
            return True
        C0.append(value[0])                
        C1.append(value[1])                
        C2.append(value[2])                
        D00_22.append(value[key])          
        D02_20.append(value[abs(key - 2)]) 
    return any([C0 == X, C0 == O,
           C1 == X, C1 == O,
           C2 == X, C2 == O,
           D00_22 == X, D00_22 == O,
           D02_20 == X, D02_20 == O])       

print()
print("крестики нолики")

show_game_field(game_field)     

while True:    
    move_counter += 1   

    if move_counter == 10:    
        print("Ничья!")
        break

    
    current_player = 'O' if move_counter % 2 == 0 else 'X'

    
    if not move_counter % 2 == 0:
        print(f"-------------==Раунд {1 if move_counter == 1 else int((move_counter + 1)/2)}==-------------")
    print(f"Игрок {current_player}")

    while True:    
        row = int(input("Введите номер строки: "))
        while not row in field_numbers:    
            print("Введен неверный номер строки!")
            row = int(input("Введите номер строки: "))

        column = int(input("Введите номер столбца: "))
        while not column in field_numbers: 
            print("Введен неверный номер столбца!")
            column = int(input("Введите номер столбца: "))

        if not game_field[row][column] == '-':   
            print("Место занято! Переходите!")
        else:
            game_field[row][column] = current_player  
            break

    show_game_field(game_field)  
    if game_over(game_field):  
        print(f"Игрок {current_player} побеждает на {move_counter} ходу!") 
        break






