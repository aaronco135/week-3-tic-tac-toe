def validate_input(num):
    try : 
        int(num)
        if num not in ['1','2','3','4','5','6','7','8','9']:
            return False
        return True
    except ValueError:
        print("enter a number int only!")
        
        
def check_x_o(x_bool):
    if x_bool == True:
        return 'X'
    else : return 'O'

def check_win(tic_tac_toe_win):
    list_of_win_index = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for combinason in list_of_win_index:
        a,b,c = combinason
        if tic_tac_toe_win[a] is not None and tic_tac_toe_win[a] == tic_tac_toe_win[b] and tic_tac_toe_win[a] == tic_tac_toe_win[c]:
            return True
    return False