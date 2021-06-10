import player_test
import computer_test
import test
import computer_start

dic = ["D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13",

"H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13",

"C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13",

"S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13"]

left_over = []

common_set, player_dic, computer_dic = test.assign(dic)

common_set, computer_dic, left_over= computer_start.computer_start(common_set, computer_dic, left_over)

victory = False

# counter = 0

while victory == False:

    common_set, player_dic, left_over, player_solved = player_test.player_test(common_set, player_dic, left_over)
    if player_solved == 4:
        print("Player won")
        victory = True
    else:
        pass
    
    print("""
Computer is Playing now""")

    common_set, computer_dic, left_over, comp_solved = computer_test.computer_test(common_set, computer_dic, left_over)
    if comp_solved == 4:
        print("Computer Won")
        victory = True
    else:
        pass

    # counter += 1




