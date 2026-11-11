from validate import check_x_o , check_win , validate_input

def main():
    win = False
    tic_tac_toe = [1,2,3,4,5,6,7,8,9]
    tic_tac_toe_win = [None,None,None,None,None,None,None,None,None]
    is_x = True
    while not win:
        if None not in tic_tac_toe_win:
            print("teko ! game over")
            break
        print(f"""
        [{tic_tac_toe[0]}] | [{tic_tac_toe[1]}] | [{tic_tac_toe[2]}]
      ------+-------+----
        [{tic_tac_toe[3]}] | [{tic_tac_toe[4]}] | [{tic_tac_toe[5]}]
      ------+-------+----
        [{tic_tac_toe[6]}] | [{tic_tac_toe[7]}] | [{tic_tac_toe[8]}]""")
        user_input = input("enter a position into the game ...")
        if not validate_input(user_input):
            print("enter a number btw 1-9 only !!")
            continue
        user_input = int(user_input)
        if tic_tac_toe_win[user_input-1] == None:
            tic_tac_toe[user_input-1] = check_x_o(is_x)
            tic_tac_toe_win[user_input-1] = check_x_o(is_x)
            if check_win(tic_tac_toe_win):
                print(f'{check_x_o(is_x)} is winning !')
                win = True
            is_x = not is_x
        else : print("this place has been already choosen , pls try again")
main()


