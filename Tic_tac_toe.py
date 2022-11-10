l1 = "1│2│3"
l2 = "4│5│6"
l3 = "7│8│9"
divisor = "─┼─┼─"
game = False
opt = ["1","2","3","4","5","6","7","8","9"]
def valid_input():
    x = input()
    if x in opt:
        print("good")
        opt.remove(x)
        return int(x)
    else:
        print("invalid")
        return valid_input()
def game_move(a,b):
    if a%3 == 0:
        globals()['l'+str(a//3)] = globals()['l'+str(a//3)][0:4]+b
    if a%3 == 1:
        globals()['l'+str((a+2)//3)] = b+globals()['l'+str((a+2)//3)][1:]
    if a%3 == 2:
        globals()['l'+str((a+1)//3)] = globals()['l'+str((a+1)//3)][:2]+b+globals()['l'+str((a+1)//3)][3:]
def game_print():
    print(l1)
    print(divisor)
    print(l2)
    print(divisor)
    print(l3)
def game_win_check(a,b,c):
    for i in range(1,4):
        if globals()['l'+str(i)][0]+globals()['l'+str(i)][2]+globals()['l'+str(i)][4] == a*3:
            print("Player",c,"won")
            return True
    for i in range(0,5,2):
        if l1[i]+l2[i]+l3[i] == a*3:
            print("Player",c,"won")
            return True
    if l1[0]+l2[2]+l3[4] == a*3:
        print("Player",c,"won")
        return True
    if l3[0]+l2[2]+l1[4] == a*3:
        print("Player",c,"won")
        return True
    if len(b) == 0:
        print("Stalemate")
        return True
game_print()
while game == False:
    print("Player 1 input:")
    inp = valid_input()
    game_move(inp,"x")
    game_print()
    if game_win_check("x",opt,1) == True:
        game = True
    if game == True:
        break
    print("Player 2 input:")
    inp = valid_input()
    game_move(inp,"o")
    game_print()
    if game_win_check("o",opt,2) == True:
        game = True